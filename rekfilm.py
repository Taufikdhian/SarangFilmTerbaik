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

# Judul halaman
cover = Image.open('cover.jpg')
st.image(cover)
st.write('Selamat datang di Website kami ! Disini kami menyediakan rekomendasi film-film action terbaik sepanjang masa. Silahkan masukan nama Film untuk mengetahui apakah film tersebut kami rekomendasikan atau tidak !')


# Kolom pencarian
search_query = st.text_input('Cari Film:')
filtered_data = df[df['movie_name'].str.contains(search_query, case=False)]

# Tampilkan hasil pencarian
st.subheader('Hasil Pencarian:')


# Berikan rekomendasi berdasarkan rating
if not filtered_data.empty:
    for index, row in filtered_data.iterrows():
        st.subheader(f"{row['movie_name']} ( {row['year']} ) ★ {row['rating']} ")
        st.write(f"{row['movie_name']}  {row['Kluster']}!",  end=" ")
        st.write(f"{row['movie_name']} adalah Film tahun {row['year']} bergenre {row['genre']} dengan rating {row['rating']}.", end=" ")
        st.write(f"Direktor dari film ini adalah  {row['director']}.",  end=" ")
        st.write(f"Actor film ini diantaranya adalah {row['star']}.",  end=" ")
        st.write(f"Deskripsi Film {row['movie_name']} : {row['description']}",  end=" ")
        st.write("----------------------------------------------------------------------")
        


