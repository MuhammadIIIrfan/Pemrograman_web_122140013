# --- Program Penghitung BMI ---
print("Program Penghitung BMI")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))

bmi = berat / (tinggi ** 2)
print(f"BMI Anda: {bmi:.2f}")

if bmi < 18.5:
    kategori = "Berat badan kurang"
elif bmi < 25:
    kategori = "Berat badan normal"
elif bmi < 30:
    kategori = "Berat badan berlebih"
else:
    kategori = "Obesitas"

print(f"Kategori: {kategori}\n")

# --- Program Pengelolaan Data Mahasiswa ---
from tabulate import tabulate

mahasiswa = [
    {"nama": "Andi", "nim": "123", "uts": 80, "uas": 85, "tugas": 90},
    {"nama": "Budi", "nim": "124", "uts": 70, "uas": 75, "tugas": 65},
    {"nama": "Citra", "nim": "125", "uts": 60, "uas": 55, "tugas": 70},
    {"nama": "Dewi", "nim": "126", "uts": 90, "uas": 95, "tugas": 85},
    {"nama": "Eka", "nim": "127", "uts": 50, "uas": 45, "tugas": 40},
]

def hitung_nilai_akhir(m):
    return 0.3 * m["uts"] + 0.4 * m["uas"] + 0.3 * m["tugas"]

def tentukan_grade(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"

tabel = []
for m in mahasiswa:
    nilai_akhir = hitung_nilai_akhir(m)
    grade = tentukan_grade(nilai_akhir)
    m["nilai_akhir"] = nilai_akhir
    m["grade"] = grade
    tabel.append([m["nama"], m["nim"], m["uts"], m["uas"], m["tugas"], nilai_akhir, grade])

print("Data Mahasiswa:")
print(tabulate(tabel, headers=["Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Grade"]))

tertinggi = max(mahasiswa, key=lambda x: x["nilai_akhir"])
terendah = min(mahasiswa, key=lambda x: x["nilai_akhir"])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"{tertinggi['nama']} ({tertinggi['nim']}) - Nilai Akhir: {tertinggi['nilai_akhir']:.2f}")

print("Mahasiswa dengan nilai terendah:")
print(f"{terendah['nama']} ({terendah['nim']}) - Nilai Akhir: {terendah['nilai_akhir']:.2f}\n")

# --- File: math_operations.py ---
# Simpan kode ini dalam file bernama math_operations.py

def luas_persegi(s):
    return s * s

def keliling_persegi(s):
    return 4 * s

def luas_persegi_panjang(p, l):
    return p * l

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def luas_lingkaran(r):
    return PI * r * r

def keliling_lingkaran(r):
    return 2 * PI * r

def celsius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_ke_kelvin(c):
    return c + 273.15

PI = 3.14159

# --- File: main.py ---
# Simpan kode ini dalam file bernama main.py

import math_operations as mo
from math_operations import luas_lingkaran, keliling_lingkaran

print("--- Hasil Perhitungan Geometri ---")
print(f"Luas Persegi (s=4): {mo.luas_persegi(4)}")
print(f"Keliling Persegi (s=4): {mo.keliling_persegi(4)}")
print(f"Luas Persegi Panjang (p=5, l=3): {mo.luas_persegi_panjang(5,3)}")
print(f"Keliling Persegi Panjang (p=5, l=3): {mo.keliling_persegi_panjang(5,3)}")
print(f"Luas Lingkaran (r=7): {luas_lingkaran(7)}")
print(f"Keliling Lingkaran (r=7): {keliling_lingkaran(7)}")

print("\n--- Konversi Suhu ---")
print(f"25°C ke Fahrenheit: {mo.celsius_ke_fahrenheit(25)}")
print(f"25°C ke Kelvin: {mo.celsius_ke_kelvin(25)}")
print(f"PI Konstanta: {mo.PI}")
