# Import Libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def app():
    # Set title
    st.title('Selamat Datang di Website Prediksi Harga Mobil')
    st.image('app_img.png', caption='Source = https://ksa.yallamotor.com/used-cars', use_column_width=True)
    st.header('Exploratory Data Analysis Section')
    
    # Load data
    df = pd.read_csv('Dataset Final.csv')

    # Plot and detail jumlah mobil per brand
    brand_counts = df['Brand'].value_counts().nlargest(10)
    brand_counts_df = brand_counts.to_frame().transpose()

    st.write("""
    ## Perbandingan 10 Brand Mobil Terbanyak
    """)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(brand_counts.index, brand_counts.values, color='skyblue')
    plt.xticks(rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig)

    st.write("""
    ## Detail Jumlah Mobil per Brand
    """)
    st.write(brand_counts_df)

    # Count Gear Type values and take top 10
    gear_counts = df['Gear Type'].value_counts().nlargest(10)

    # Plot and detail jumlah mobil per Gear Type
    st.write("""
    ## Perbandingan 10 Gear Type Mobil Terbanyak
    """)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(gear_counts.index, gear_counts.values, color='skyblue')
    plt.title('Perbandingan 10 Gear Type Mobil Terbanyak')
    plt.xlabel('Gear Type')
    plt.ylabel('Jumlah Mobil')
    plt.xticks(rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.6)
    st.pyplot(fig)

    st.write("""
    ## Detail Jumlah Mobil per Gear Type
    """)
    gear_counts_df = gear_counts.to_frame().transpose()
    st.write(gear_counts_df)
