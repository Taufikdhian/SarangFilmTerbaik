import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

df = pd.read_csv('datafilm.csv')

# Menentukan jumlah kluster (k=3)
kmeans = KMeans(n_clusters=3, random_state=42)
df['Kluster'] = kmeans.fit_predict(df[['rating']])

# Memberikan nama kluster berdasarkan kriteria rekomendasi
df['Kluster'] = df['Kluster'].map({0: 'Sangat Direkomendasikan', 1: 'Kurang Direkomendasikan', 2: 'Cukup Direkomendasikan'})

poster1 = Image.open('poster1.jpg')
poster2 = Image.open('poster2.jpg')
poster3 = Image.open('poster3.jpg')
poster4 = Image.open('poster4.jpg')
poster5 = Image.open('poster5.jpg')
poster6 = Image.open('poster6.jpg')
poster7 = Image.open('poster7.jpg')
poster8 = Image.open('poster8.jpg')
poster9 = Image.open('poster9.jpg')
poster10 = Image.open('poster10.jpg')

st.title('TOP 10!')
st.subheader('Top 10 Film Action Versi Sarang Film Terbaik')
st.write('Dibawah ini adalah 10 film action terbaik sepanjang masa. 10 Film ini sangat kami rekomendasikan untuk kamu tonton. Penentuan TOP 10 ini berdasarkan rating dari masing-masing film yang didapat. Dengan kata lain urutan list dibawah ini adalah TOP 10 Film action dengan rating tertinggi sepanjang masa !')


st.subheader('1. The Lord of the Rings: The Return of the King')
st.image(poster1, width=250)
st.subheader('2. The Dark Knight')
st.image(poster2, width=250)
st.subheader('3. The Lord of the Rings: The Fellowship of the Ring')
st.image(poster3, width=250)
st.subheader('4. Inception')
st.image(poster4, width=250)
st.subheader('5. The Lord of the Rings: The Two Towers')
st.image(poster5, width=250)
st.subheader('6. The Matrix')
st.image(poster6, width=250)
st.subheader('7. Star Wars: Episode V - The Empire Strikes Back')
st.image(poster7, width=250)
st.subheader('8. Terminator 2: Judgment Day')
st.image(poster8, width=250)
st.subheader('9. Seven Samurai')
st.image(poster9, width=250)
st.subheader('10. Star Wars')
st.image(poster10, width=250)

st.subheader('Film Action Lainnya Berdasarkan Urutan Rating Tertinggi :')

df_urut = df.sort_values(by='rating', ascending=False)
st.dataframe(df_urut[['movie_name', 'year', 'rating']])

