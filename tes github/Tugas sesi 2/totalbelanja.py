def hitung_uang_kembalian(total_belanja, jumlah_pembayaran):
    if jumlah_pembayaran < total_belanja:
        return "Maaf, jumlah pembayaran tidak mencukupi."
    
    uang_kembalian = jumlah_pembayaran - total_belanja
    return uang_kembalian

# Input data belanja
total_belanja = float(input("Masukkan Total Belanja: "))
jumlah_pembayaran = float(input("Masukkan Jumlah Pembayaran: "))

# Hitung uang kembalian
hasil_kembalian = hitung_uang_kembalian(total_belanja, jumlah_pembayaran)

# Tampilkan hasil
if isinstance(hasil_kembalian, str):
    print(hasil_kembalian)
else:
    print("\nUang Kembalian: Rp", hasil_kembalian)
