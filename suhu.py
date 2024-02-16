def konversi_suhu_reamur_ke_celcius(reamur):
    celcius = (5/4) * reamur
    return celcius

def konversi_celcius_ke_fahrenheit(celcius):
    fahrenheit = (9/5) * celcius + 32
    return fahrenheit

def konversi_celcius_ke_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

# Input suhu dalam Reamur
reamur_input = float(input("Masukkan suhu dalam Reamur: "))

# Konversi ke Celcius, Fahrenheit, dan Kelvin
celcius_output = konversi_suhu_reamur_ke_celcius(reamur_input)
fahrenheit_output = konversi_celcius_ke_fahrenheit(celcius_output)
kelvin_output = konversi_celcius_ke_kelvin(celcius_output)

# Menampilkan hasil konversi
print(f"{reamur_input} Reamur sama dengan {celcius_output:.2f} Celcius")
print(f"{celcius_output:.2f} Celcius sama dengan {fahrenheit_output:.2f} Fahrenheit")
print(f"{celcius_output:.2f} Celcius sama dengan {kelvin_output:.2f} Kelvin")
