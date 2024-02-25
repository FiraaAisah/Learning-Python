def hitung_kembalian(total_belanja, uang_dibayar):
    # Berlaku diskon 10% jika total belanja lebih dari 70 ribu
    if total_belanja > 70000:
        diskon = 0.1
        total_belanja -= total_belanja * diskon
    
    if uang_dibayar < total_belanja:
        print("Maaf, uang yang dibayar kurang.")
        return
    
    kembalian = uang_dibayar - total_belanja
    
    # Daftar nilai kembalian yang mungkin
    pecahan_uang = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    print("Kembalian:")
    
    for nilai in pecahan_uang:
        jumlah_pecahan = kembalian // nilai
        if jumlah_pecahan > 0:
            print(f"{nilai} x {jumlah_pecahan}")
            kembalian %= nilai
    
    return kembalian

# Contoh penggunaan
total_belanja = float(input("Total belanja: "))
uang_dibayar = float(input("Uang yang dibayar: "))

sisa_kembalian = hitung_kembalian(total_belanja, uang_dibayar)

print(f"Sisa kembalian yang tidak dapat dipecah: {sisa_kembalian}")
