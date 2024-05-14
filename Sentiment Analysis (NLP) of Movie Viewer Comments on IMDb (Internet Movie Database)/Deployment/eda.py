# Import Libraries
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_word_cloud(df, lbl):
    figsize=(14.7, 7.35)

    text = ' '.join(df[df['label'] == lbl]['text'])
    wordcloud = WordCloud(width=int(figsize[0]*100), height=int(figsize[1]*100), background_color='white').generate(text)

    plt.figure(figsize=figsize)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def app():
    # Set title
    st.title('Exploratory Data Analysis Page')
    
    # Load data
    df = pd.read_csv('movie.csv')


    # The Most Frequent Label
    st.header("""The Most Frequent Label""")
    label_mode = df['label'].mode()
    st.write('Label Sentimen Paling Banyak Adalah',label_mode[0],', label 0 = Sentimen Negatif')
    
    st.header('Makna Label:')
    st.write('1 = Positive, 0 = Negative')

    # Plot and detail jumlah kata per teks
    st.header('Word Count')
    df['word_count'] = df['text'].apply(lambda x: len(x.split()))

    # Menampilkan detail jumlah kata per teks
    st.write("Detail Jumlah Kata per Teks:")
    st.write(df[['text', 'word_count']])


    def plot_target_hist(df, col):
        outcome_counts = df[col].value_counts()
        total = outcome_counts.sum()
        outcome_percentages = outcome_counts / total * 100
    
        fig, ax = plt.subplots(figsize=(3.5, 3.5))
        outcome_counts.plot(kind='bar', ax=ax)
        ax.set_xticklabels(outcome_counts.index, rotation=0, fontsize=9)
        ax.set_yticks(range(0, max(outcome_counts) + 1, 5000))
        ax.set_yticklabels(range(0, max(outcome_counts) + 1, 5000), fontsize=9)
        ax.set_xlabel(None)

        for i, percentage in enumerate(outcome_percentages):
            ax.text(i, outcome_counts[i], f'{percentage:.2f}%', ha='center', va='bottom', fontsize=8)

        st.pyplot(fig)

    def plot_col_hist(df, col):
        fig, ax = plt.subplots(figsize=(14, 3.5))
        ax.hist(df[df['label'] == 1][col], bins=50, alpha=0.6, color='#1F77B4', label='1')
        ax.hist(df[df['label'] == 0][col], bins=50, alpha=0.6, color='#D62728', label='0')
        ax.tick_params(labelsize=9)
        ax.set_xticks(range(0, max(df[col])+1, 250))
        ax.legend(fontsize=8)
    
        st.pyplot(fig)

    ### Univariate Analysis
    st.header('Univariate Analysis')
    plot_target_hist(df, 'label')

    ### Multivariate Analysis
    st.header('Multivariate Analysis')
    plot_col_hist(df, 'word_count')


if __name__ == "__main__":
    app()
