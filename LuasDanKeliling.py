import math

def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

def hitung_keliling_segitiga(sisi1, sisi2, sisi3):
    keliling = sisi1 + sisi2 + sisi3
    return keliling

# Input panjang alas, tinggi, dan sisi-sisi segitiga
alas_input = float(input("Masukkan panjang alas segitiga: "))
tinggi_input = float(input("Masukkan tinggi segitiga: "))
sisi1_input = float(input("Masukkan panjang sisi pertama segitiga: "))
sisi2_input = float(input("Masukkan panjang sisi kedua segitiga: "))
sisi3_input = float(input("Masukkan panjang sisi ketiga segitiga: "))

# Hitung luas dan keliling segitiga
luas_output = hitung_luas_segitiga(alas_input, tinggi_input)
keliling_output = hitung_keliling_segitiga(sisi1_input, sisi2_input, sisi3_input)

# Menampilkan hasil
print(f"Luas segitiga: {luas_output:.2f} satuan luas")
print(f"Keliling segitiga: {keliling_output:.2f} satuan panjang")
