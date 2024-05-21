import streamlit as st
import re

st.title('Kalkulator Berat Molekul')
    
def hitung_berat_molekul(rumus, berat_atom):
        berat_molekul = 0
        unsur = re.findall(r'([A-Z][a-z]*)(\d*)', rumus)
        for unsur, jumlah in unsur:
            jumlah = int(jumlah) if jumlah else 1
            berat_molekul += berat_atom[unsur] * jumlah
            
        return berat_molekul
    
berat_atom = {
        "H": 1.0079,
        "He" : 4.0026,
        "Li" : 6.941,
        "Be" : 9.0122,
        "B" : 10.811,
        "C": 12.011,
        "O": 15.999,
        "N": 14.007,
        "F" : 18.998,
        "Ne" : 20.180,
        "Na" : 22.990,
        "Mg" : 24.305,
        "Al" : 26.982,
        "Si" : 28.086,
        "P" : 30.974,
        "S": 32.065,
        "Cl": 35.453,
        "Ar" : 39.948,
        "K" : 39.098,
        "Ca" : 40.078,
        "Sc" : 44.956,
        "Ti" : 47.867,
        "V" : 50.942,
        "Cr" : 51.996,
        "Mn" : 54.938,
        "Fe" : 55.845,
        "Co" : 58.933,
        "Ni" : 58.963,
        "Cu" : 63.546,
        "Zn" : 65.38,
        "Ga" : 69.723,
        "Ge" : 72.64,
        "As" : 74.922,
        "Se" : 78.96,
        "Br" : 79.904,
        "Kr" : 83.798,
        "Rb" : 85.468,
        "Sr" : 87.62,
        "Y" : 88.906,
        "Zr" : 91.224,
        "Nb" : 92.906,
        "Mo" : 95.96,
        "Ru" : 101.07,
        "Rh" : 102.91,
        "Pd" : 106.42,
        "Ag" : 107.87,
        "Cd" : 112.41,
        "In" : 114.82,
        "Sn": 118.71,
        "Sb": 121.76,
        "Te" : 127.60,
        "I" : 126.90,
        "Xe": 131.29,
        "Cs": 132.91,
        "Ba": 137.33,
        "La": 138.91,
        "Ce": 140.12,
        "Pr": 140.91,
        "Nd": 144.24,
        "Sm": 150.36,
        "Eu": 151.96,
        "Gd": 157.25,
        "Tb": 158.93,
        "Dy": 162.90,
        "Ho": 164.93,
        "Er": 167.26,
        "Tm": 168.93,
        "Yb": 173.05,
        "Lu": 174.97,
        "Hf": 178.49,
        "Ta": 180.95,
        "W": 183.84,
        "Re": 186.21,
        "Os": 190.23,
        "Ir": 192.22,
        "Pt": 195.08,
        "Au": 196.97,
        "Hg": 200.59,
        "Tl" : 204.38,
        "Pb" : 207.2,
        "Bi" : 208.98,
        "Th" :232.04,
        "Pa" : 231.04,
        "U" : 238.03 
}
rumus_input = st.text_input('Masukkan Rumus Senyawa Kimia (Contoh: H2O, C6H12O6):')
    
if rumus_input:
   berat_molekul = hitung_berat_molekul(rumus_input, berat_atom)
   st.write('Berat molekul dari', rumus_input, 'adalah', berat_molekul, 'g/mol.')