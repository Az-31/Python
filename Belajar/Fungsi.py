##membuat fungsi
'''
def nama_fungsi(argument):
    badan fungsi
'''
# def tambah(angka1,angka2):
#     hasil = angka1 + angka2
#     print(f"{angka1} + {angka2} = {hasil}")

# tambah(1,5)
# tambah(10000,1)

import os

# os.system("cls")

# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# ##Steal input
# LEBAR = int(input('Masukkan nilai lebar:'))
# PANJANG = int(input('Masukkan nilai panjang:'))

# #
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# print(f"Hasil perhitungan luas = {LUAS}")
# print(f"Hasil perhitungan keliling = {KELILING}")


def header():
    os.system("cls")

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    lebar = int(input('Masukkan nilai lebar: '))
    panjang = int(input('Masukkan nilai panjang: '))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    return 2*(lebar*panjang)

while True:
    header()
    lebar,panjang = input_user()
    luas = hitung_luas(lebar,panjang)
    keliling = hitung_keliling(lebar,panjang)

    print(f"Hasil perhitungan luas = {luas}")
    print(f"Hasil perhitungan keliling = {keliling}")

    isContinue = input("Apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print('Program tamattt.')