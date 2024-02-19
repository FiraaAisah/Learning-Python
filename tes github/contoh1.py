def hitung_total_biaya(jumlah_jeruk, jumlah_apel, jumlah_mangga, jumlah_manggis, jumlah_durian):
    harga_jeruk = 15000
    harga_apel = 30000
    harga_mangga = 20000
    harga_manggis = 7000
    harga_durian = 50000

    total_biaya = (jumlah_jeruk * harga_jeruk) + (jumlah_apel * harga_apel) + (jumlah_mangga * harga_mangga) + (jumlah_manggis * harga_manggis) + (jumlah_durian * harga_durian)
    
    return total_biaya

# Input data jumlah buah
jumlah_jeruk = float(input("Masukkan jumlah kilogram jeruk: "))
jumlah_apel = float(input("Masukkan jumlah kilogram apel: "))
jumlah_mangga = float(input("Masukkan jumlah kilogram mangga: "))
jumlah_manggis = float(input("Masukkan jumlah kilogram manggis: "))
jumlah_durian = float(input("Masukkan jumlah buah durian: "))

# Hitung total biaya
total_biaya = hitung_total_biaya(jumlah_jeruk, jumlah_apel, jumlah_mangga, jumlah_manggis, jumlah_durian)

# Tampilkan hasil
print("\nTotal biaya pembelian buah: Rp", total_biaya)