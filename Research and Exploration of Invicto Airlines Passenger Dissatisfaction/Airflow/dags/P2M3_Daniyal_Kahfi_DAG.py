'''
=================================================
Milestone 3

Nama  : Daniyal Kahfi
Batch : FTDS-029-RMT

Program ini dibuat untuk melakukan automatisasi load data dari PostgreSQL, data cleaning dan 
posting data ke Elasticsearch untuk dilakukan visualisasi data.
Data yang digunakan pada program ini merupakan data kepuasan penumpang invistico airline.

=================================================
'''

import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

import pandas as pd
import psycopg2
from elasticsearch import Elasticsearch

def fetchData():

    '''
    Fungsi ini ditujukan untuk mengambil data dari PostgreSQL dan melakukan convert data.
    Fungsi ini akan menghasilkan file csv yang selanjutnya digunakan untuk Cleaning data

    Contoh penggunaan:
    fetchData()
    '''


    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
    )
    sql = 'SELECT * FROM table_m3;'
    df = pd.read_sql(sql, conn)
    df.to_csv('/opt/airflow/dags/P2M3_DaniyalKahfi_data_raw.csv', sep=',', index=False, na_rep='NA')
    conn.close()

def data_cleaning():
    ''' Fungsi ini digunakan untuk membersihkan dataframe dengan men drop duplikat, 
    mengubah huruf pada judul kolom menjadi lowercase, mengganti spasi dengan underscore,
    menghapus simbol dan juga handling missing value'''
    df=pd.read_csv('/opt/airflow/dags/P2M3_DaniyalKahfi_data_raw.csv')
    df.drop_duplicates(inplace=True) # Handling Duplikat
    df.columns = df.columns.str.lower()  # Ubah semua huruf menjadi lowercase
    df.columns = df.columns.str.replace(' ', '_')  # Ganti spasi dengan underscore
    df.columns = df.columns.str.replace(r'[^a-zA-Z0-9_]', '')  # Hapus simbol tidak diperlukan
    df.dropna(inplace=True)  # Drop missing value
    df.to_csv('/opt/airflow/dags/P2M3_DaniyalKahfi_data_clean.csv', index = False)



def insertElasticsearch():
    ''' Fungsi ini digunakan untuk menaruh data yang sudah bersih ke elasticsearch agar
    bisa dibuka di kibana'''
    es = Elasticsearch("http://elasticsearch:9200", timeout=60)  # Timeout diperpanjang menjadi 60 detik
    df=pd.read_csv('/opt/airflow/dags/P2M3_DaniyalKahfi_data_clean.csv')
    for i,r in df.iterrows():
        doc=r.to_json()
        res=es.index(index="for_milestone_kibana",doc_type="doc",body=doc)
        print(res)
	

default_args= {
    'owner': 'DaniyalKahfi',
    'start_date': dt.datetime(2024, 4, 29, 6, 37, 0) - timedelta(hours=7)
}

with DAG(
    "P2M3_DaniyalKahfi_DAG",
    description='Fetching Data, Cleaning Data, and Post to Elasticsearch',
    schedule_interval='30 6 * * *',
    default_args=default_args,
    # dagrun_timeout=timedelta(seconds=300)
    ) as dag:

    fetch_data = PythonOperator(
        task_id='fetch_data',
        python_callable=fetchData,
    )

    clean_data = PythonOperator(
        task_id='clean_data',
        python_callable=data_cleaning,
    )
    
    post_data = PythonOperator(
        task_id='post_data_Elasticsearch',
        python_callable=insertElasticsearch
    )


    fetch_data >> clean_data >> post_data