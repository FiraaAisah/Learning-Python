algoritma =float(input("masukan nilai anda :"))
objek =float(input("masukan nilai anda :"))
kalkulus =float(input("masukan nilai anda :"))
database =float(input("masukan nilai anda :"))
etika =float(input("masukan nilai anda :"))
english =float(input("masukan nilai anda :"))

def skortobobot (skor):
    if skor >= 90:
        return 4
    elif skor >= 85:
        return 3.75
    elif skor >= 80:
        return 3.50
    elif skor >= 75:
        return 3.25
    elif skor >= 70:
        return 3
    elif skor >= 65:
        return 2.75
    elif skor >= 60:
        return 2.5
    elif skor >= 55:
        return 2.25
    elif skor >= 50:
        return 2
    elif skor >= 45:
        return 1.75
    elif skor >= 40:
        return 1.5
    elif skor >= 35:
        return 1.25
    elif skor >= 30:
        return 1
    else:
        return 0
    
nilai_kredit = 3

total_algoritma = nilai_kredit * skortobobot(algoritma)
total_objek = nilai_kredit * skortobobot(objek)
total_kalkulus = nilai_kredit * skortobobot(kalkulus)
total_database = nilai_kredit * skortobobot(database)
total_etika = nilai_kredit * skortobobot(etika)
total_english = nilai_kredit * skortobobot(english)

total_bobot = total_algoritma + total_objek + total_kalkulus + total_database + total_etika + total_english

def countIps(totalSkor, totalKredit):
    total_ipk = totalSkor / totalKredit
    return total_ipk

print("IPK anda adalah: ", countIps(total_bobot, 18))