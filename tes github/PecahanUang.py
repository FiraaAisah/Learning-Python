def hitung_pecahan_uang(jumlah_uang):
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
    
    for nilai in pecahan:
        jumlah_pecahan = jumlah_uang // nilai
        if jumlah_pecahan > 0:
            print(f"1 lembar {nilai} ribuan = {jumlah_pecahan}")
            jumlah_uang %= nilai

# Contoh penggunaan
jumlah_uang = int(input("Masukkan jumlah uang: "))
hitung_pecahan_uang(jumlah_uang)
