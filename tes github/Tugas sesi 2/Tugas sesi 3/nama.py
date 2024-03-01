print("=== Form Pendaftaran Universitas ===")

nama = input("Nama: ")
tempat_lahir = input("Tempat Lahir: ")
tanggal_lahir = int(input("Tanggal Lahir: "))
tahun_lahir = int(input("Tahun Lahir: "))

umur = 2024 - tahun_lahir
if bulan_lahir.lower() == 'februari' and tanggal_lahir > 28:
    umur -= 1

nilai_english = float(input("Nilai English: "))
nilai_mtk = float(input("Nilai Mtk: "))
nilai_indonesia = float(input("Nilai Indonesia: "))

jenis_kelamin = input("Jenis Kelamin (Laki-laki/Perempuan): ")

rata_rata_nilai = (nilai_english + nilai_mtk + nilai_indonesia) / 3

if umur < 25:
    if rata_rata_nilai >= 80:
        if jenis_kelamin.lower() == 'laki-laki':
            jurusan_terpilih = 'Jurusan Teknik Informatika'
        elif jenis_kelamin.lower() == 'perempuan':
            jurusan_terpilih = 'Jurusan Sistem Informasi'
        else:
            jurusan_terpilih = 'Jurusan DKV'
        print(f"Selamat, {nama}! Anda direkomendasikan masuk ke {jurusan_terpilih}.")
    else:
        print("Maaf, rata-rata nilai Anda kurang dari 80. Silakan coba lagi.")
else:
    print("Maaf, Anda tidak memenuhi syarat umur untuk mendaftar.")
