##Latihan??

#menggunakan for
print('FOR')
sisi = 15

tambah = 1
for i in range(sisi):
    print('*'*tambah)
    tambah += 1

print('+===================+')
#menggunakan while
print('WHILE')
tambah = 1

while True:
    print('*'*tambah)
    tambah +=1

    if tambah > sisi:
        break

print('+===================+')
#menggunakan while ganjil
print('WHILE')
tambah = 1

while True:
    if (tambah%2):  #ganjil
        print('*'*tambah)
        tambah +=1
    else:
        tambah += 1
        continue
    if tambah > sisi:
        break

print('+===================+')

#menggunakan while ganjil
print('WHILE')
tambah = 1
spasi = int(sisi/2)

while True:
    if (tambah%2):  #ganjil
        print(' '*spasi,'*'*tambah)
        spasi -=1
        tambah +=1
    else:
        tambah += 1
        continue
    if tambah > sisi:
        break

print('+===================+')

