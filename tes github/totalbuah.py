harga_buah = {
    'Jeruk': 15000,
    'Apel': 30000,
    'Mangga': 20000,
    'Manggis': 7000,
    'Durian': 50000
}

jumlah_buah = {
    'Jeruk': 3,
    'Apel': 2,
    'Mangga': 0,
    'Manggis': 5,
    'Durian': 2
}

def hitung_total_belanja(harga_buah, jumlah_buah):
    total_belanja = 0
    
    for buah, jumlah in jumlah_buah.items():
        if buah in harga_buah:
            harga_per_unit = harga_buah[buah]
            total_belanja += harga_per_unit * jumlah
            if 'kilo' in buah:
                print(f"{jumlah} {buah} = {harga_per_unit * jumlah}")
            elif 'buah' in buah:
                print(f"{jumlah} {buah} = {harga_per_unit * jumlah}")
    
    print(f"Total belanja = {total_belanja}")
hitung_total_belanja(harga_buah, jumlah_buah)
