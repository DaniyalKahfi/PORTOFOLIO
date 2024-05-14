import pandas as pd
import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

def app():
    model = load_model('model_new.keras')
    # st.header('Silahkan Masukkan Review Film IMDB yang pernah Anda Saksikan Menggunakan Bahasa Inggris!')
    
    # Input form
    with st.form ('Silahkan Masukkan Review Film IMDB yang pernah Anda Saksikan Menggunakan Bahasa Inggris!'):
        text = st.text_input('disini ya')
        sub= st.form_submit_button('Submit Review')

        # Jika tombol Submit ditekan
        if sub:
            # Membuat data input
            data_inf = {
                'text': [text],
            }
            df = pd.DataFrame(data_inf)

            # Memprediksi menggunakan model
            prediksi = model.predict(df)
            pred_inf=np.where(prediksi >= 0.5, 1, 0)
            labels = ['Sentimen Negatif', 'Sentimen Positif']
            hasil = ""
            for i in range(len(pred_inf[0])):
                if pred_inf[0][i] == 1:
                    hasil = labels[i]

            st.write('Review Kamu Terkategori',hasil)
if __name__ == "__main__":
    app()