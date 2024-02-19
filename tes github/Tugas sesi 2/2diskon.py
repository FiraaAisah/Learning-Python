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

# Berikan diskon 10% jika total gaji lebih dari 70 ribu
if total_gaji > 70000:
    diskon = 0.1 * total_gaji
    total_gaji -= diskon
    print("\nAnda mendapatkan diskon 10%!")
    print("Total Gaji Karyawan (setelah diskon): Rp", total_gaji)
else:
    print("\nTotal Gaji Karyawan: Rp", total_gaji)

