import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/ACER/Documents/kuliah/s5/Apk Web/Streamlit/datafilm.csv')


# Menentukan jumlah kluster (k=3)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Kluster'] = kmeans.fit_predict(df[['rating']])

# Memberikan nama kluster berdasarkan kriteria rekomendasi
df['Kluster'] = df['Kluster'].map({0: 'Sangat Direkomendasikan', 1: 'Kurang Direkomendasikan', 2: 'Cukup Direkomendasikan'})

# Judul halaman
st.title('Kluster Film')
st.write("Berikut merupakan daftar film yang sudah kita pilah menjadi 3 kluster besar tergantung tingkat kerekomendasian film(sangat direkomendasikan, cukup direkomendasikan, dan kurang direkomendasikan). Pemilahan Film dilakukan menggunakan sistem otomatis untuk menciptakan sistem rekomendasi yang baik")

# Tampilkan tabel untuk setiap kluster
for kluster_id in range(3):
    st.subheader(f'{df["Kluster"].unique()[kluster_id]}')
    st.dataframe(df[df['Kluster'] == df["Kluster"].unique()[kluster_id]][['movie_name', 'year', 'rating']])

