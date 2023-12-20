import streamlit as st
from PIL import Image


st.title('Sarang Film Terbaik')

st.subheader('Tentang Website')
st.write('Sarang Film Terbaik adalah platform daring yang didedikasikan untuk memberikan rekomendasi film action terbaik kepada para penikmat film. Dengan desain yang bersih dan antarmuka yang ramah pengguna, Sarang Film Terbaik memberikan pengalaman yang menyenangkan bagi para pengguna yang mencari film action berkualitas tinggi. Dengan komitmen untuk memberikan pengalaman terbaik kepada pengguna, Sarang Film Terbaik menjadi tempat ideal bagi para pecinta film action untuk mengeksplorasi, menemukan, dan menikmati film-film seru secara maksimal. Selamat menikmati serangkaian petualangan sinematik yang tak terlupakan di Sarang Film Terbaik!')

st.subheader('Metode Sistem Rekomendasi')
st.write('Sarang Film Terbaik menerapkan metode sistem rekomendasi yang canggih menggunakan teknik klustering K-Means untuk mengelompokkan rating film ke dalam tiga kluster berbeda. Dengan dataset yang mengandung informasi rating dari 2234 film, metode ini memberikan rekomendasi yang lebih sempurna dan sesuai dengan preferensi rating yang didapat dari penikmat film di seluruh dunia.')

st.subheader('K-Means')
visualisasi = Image.open('C:/Users/ACER/Documents/kuliah/s5/Apk Web/Streamlit/visualisasi.png')
st.image(visualisasi)
st.write('Metode Klustering K-Means adalah suatu teknik analisis data yang digunakan untuk mengelompokkan sejumlah data menjadi beberapa kelompok (kluster) yang memiliki kesamaan berdasarkan karakteristik tertentu. Dalam konteks ini, K-Means mengelompokkan data ke dalam sejumlah kluster berdasarkan pola atau kemiripan dalam atribut yang diukur. K-Means biasanya digunakan untuk analisis klustering pada data numerik dan dapat diterapkan dalam berbagai konteks, termasuk analisis konsumen, pengelompokan data geografis, dan dalam hal ini, pengelompokan rating film pada sistem rekomendasi. Kelemahan K-Means melibatkan kebutuhan untuk menentukan jumlah kluster sebelumnya dan kepekaannya terhadap inisialisasi kluster awal. Meskipun demikian, K-Means tetap menjadi salah satu metode klustering yang populer dan efisien.')


st.subheader('Profil')
col1, col2 = st.columns(2)
with col1:
    profil = Image.open('C:/Users/ACER/Documents/kuliah/s5/Apk Web/Streamlit/profil.jpg')
    st.image(profil)

with col2:
    st.write('Halo! Saya adalah Taufik Dhian Kusuma NIM 215317141005, mahasiswa semester 5 Universitas Negeri Yogyakarta prodi Teknologi Informasi yang sedang mengikuti mata kuliah Praktik Aplikasi Web. Saya berdomisili di Yogyakarta.')