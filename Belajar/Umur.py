import datetime as dt


print("Masukkan tanggal, bulan, dan tahun")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir : {tanggal_lahir}")


hari_ini = dt.date.today()

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365

print(f"Hari : {tanggal_lahir:%A}")
print(f"Umur anda adalah :{umur_tahun} tahun")
