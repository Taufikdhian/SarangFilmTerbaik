import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('datafilm.csv')



# Menentukan jumlah kluster (k=3)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Kluster'] = kmeans.fit_predict(df[['rating']])

# Memberikan nama kluster berdasarkan kriteria rekomendasi
df['Kluster'] = df['Kluster'].map({0: 'Sangat Direkomendasikan', 1: 'Kurang Direkomendasikan', 2: 'Cukup Direkomendasikan'})

st.title('Semua Film')
st.write("Berikut merupakan daftar film action kita yang kita tampilkan tanpa pemilahan kluster. Namun kita berikan tambahan kolom untuk kluster sebagai pelabelan tingkat kerekomendasian tiap film.")


st.dataframe(df[['movie_name', 'year', 'rating',  'Kluster']])