import streamlit as st
import math

option = st.selectbox(
    'Menu', 
    ('Perhitungan Normalitas','Perhitungan %Kadar', 'Perhitungan Rata-rata', 'Perhitungan SD','Perhitungan %RPD','Perhitungan %RSD')
)

if option == 'Perhitungan Normalitas':
    st.title('Kalkulator Normalitas')

    jumlah_digit = 4
    bobot = st.number_input('Masukan Berat Bobot (mg)', step=1e-4, format="%.4f")
    volume = st.number_input('Masukan Volume Titran (mL)', step=1e-4, format="%.4f")
    be = st.number_input('Masukan Nilai BE/BM', step=1e-4, format="%.4f")
    fp = st.number_input('Masukan FP (Jika tidak ada isi dengan angka satu (1))', step=1e-4, format="%.4f")

    tombol = st.button('hitung nilai normalitas')
    
    if tombol:
        nilainormalitas = bobot/(fp*be*volume)
        st.success(f'Nilai Normalitas Adalah {nilainormalitas:.4f}N')

elif option == 'Perhitungan %Kadar':
    st.title('Kalkulator Perhitungan %Kadar dalam Larutan Sampel')

    jumlah_digit = 4
    volumetitran = st.number_input('Masukan Volume Titran (mL)', step=1e-4, format="%.4f")
    n = st.number_input('Masukan Normalitas Titrat', step=1e-4, format="%.4f")
    be = st.number_input('Masukan Nilai BE/BM', step=1e-4, format="%.4f")
    volumetitrat = st.number_input('Masukan Volume Titrat (mL/mg)', step=1e-4, format="%.4f")
    fp = st.number_input('Masukan FP (Jika tidak ada isi dengan angka satu (1))', step=1e-4, format="%.4f")
    
    tombol = st.button('Hitung nilai %Kadar Sampel dalam Latutan')
    
    if tombol:
        nilaikadar = (volumetitran*n*be)/volumetitrat*(10**-3*fp*100)
        st.success(f'Nilai Normalitas Adalah {nilaikadar:.4f}%')

elif option == 'Perhitungan Rata-rata':
   st.title('Kalkulator Rata-rata')
   st.write('kalkulator Perhitungan Rata-rata')
   
   jumlah_digit = 4
   rt1 = st.number_input('Masukan hasil perhitungan Normalitas/%Kadar 1', step=1e-4, format="%.4f")
   rt2 = st.number_input('Masukan hasil perhitungan Normalitas/%Kadar 2', step=1e-4, format="%.4f")
   rt3 = st.number_input('Masukan hasil perhitungan Normalitas/%Kadar 3', step=1e-4, format="%.4f")
   
   tombol = st.button('Hitung nilai rata-rata perhitungan')

   if tombol:
        nilairtrt = (rt1+rt2+rt3)/3
        st.success(f'Nilai Rata-ratanya adalah {nilairtrt:.4f}')

elif option == 'Perhitungan SD':
    st.title('Kalkulator SD')
    st.write('kalkulator Standar Deviasi dengan cara triplo')

    jumlah_digit = 4
    rn1 = st.number_input('Masukan hasil perhitungan Normalitas/%Kadar 1', step=1e-4, format="%.4f")
    rn2 = st.number_input('Masukan hasil perhitungan Normalitas/%Kadar 2', step=1e-4, format="%.4f")
    rn3 = st.number_input('Masukan hasil perhitungan Normalitas/%Kadar 3', step=1e-4, format="%.4f")
    
    tombol = st.button('Hitung nilai Standar Deviasi')
    
    if tombol:
        nilaisd = math.sqrt((((rn1-((rn1+rn2+rn3)/3))**2)+((rn2-((rn1+rn2+rn3)/3))**2)+((rn3-((rn1+rn2+rn3)/3))**2))/2)
        st.success(f'Nilai Standar Deviasi {nilaisd:.4f}')

elif option == 'Perhitungan %RPD':
    st.title('Perhitungan %RPD')
    st.write('Perhitungan %RPD (Cara Duplo)')

    jumlah_digit = 4
    x1 = st.number_input('Masukan Nilai Perhitungan 1', step=1e-4, format="%.4f")
    x2 = st.number_input('Masukan Nilai Perhitangan 2', step=1e-4, format="%.4f")
    
    tombol = st.button('Hitung nilai %RPD')
    
    if tombol:
        nilairpd = ((abs(x1-x2))/((x1+x2)/2))*100
        st.success(f'Nilai %RPD {nilairpd:.4f}%')

elif option == 'Perhitungan %RSD':
    st.title('Perhitungan %RSD')
    st.write('Perhitungan %RSD (Cara Triplo)')

    jumlah_digit = 4
    sd = st.number_input('Masukan Nilai SD', step=1e-4, format="%.4f")
    rtrt = st.number_input('Masukan Nilai Rata-rata Perhitungan', step=1e-4, format="%.4f")
    
    tombol = st.button('Hitung nilai %RSD')
    
    if tombol:
        nilairsd = (sd/rtrt)*100
        st.success(f'Nilai %RSD {nilairsd:.4f}%')

