def hitung_gaji(gaji_pokok, uang_transport, uang_makan, tunjangan_jabatan, honor_lembur):
    total_gaji = gaji_pokok + uang_transport + uang_makan + tunjangan_jabatan + honor_lembur
    return total_gaji

# Input data gaji karyawan
gaji_pokok = float(input("Masukkan Gaji Pokok: "))
uang_transport = float(input("Masukkan Uang Transport Harian: "))
uang_makan = float(input("Masukkan Uang Makan Harian: "))
tunjangan_jabatan = float(input("Masukkan Tunjangan Jabatan: "))
honor_lembur = float(input("Masukkan Honor Lembur: "))

# Hitung total gaji
total_gaji = hitung_gaji(gaji_pokok, uang_transport, uang_makan, tunjangan_jabatan, honor_lembur)

# Tampilkan hasil
print("\nTotal Gaji Karyawan: Rp", total_gaji)
