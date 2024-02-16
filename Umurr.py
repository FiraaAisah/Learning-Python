def hitung_umur(tahun_lahir):
    tahun_sekarang = 2024  # Ganti dengan tahun sekarang atau sesuai kebutuhan
    umur = tahun_sekarang - tahun_lahir
    return umur

# Input tahun lahir
tahun_lahir_input = int(input("Masukkan tahun lahir: "))

# Hitung umur
umur_output = hitung_umur(tahun_lahir_input)

# Menampilkan hasil
print(f"Umur Anda sekarang adalah {umur_output} tahun.")
