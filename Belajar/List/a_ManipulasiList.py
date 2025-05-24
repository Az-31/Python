#index   0(-3)  1(-2)   3(-1)
data = ['asep','agus','ashiap']
print(data)

#mengambil data list
data_1 = data[0]
print('data pertama (index 0) =',data_1)

last_data = data[-1]
print('data terakhir =',last_data)

#menghitung panjang list
panjang_data = len(data)
print('panjang data =',panjang_data)

#menambahkan item
'''data.insert(posisi,'item')'''
print('data sebelum di tambah',data)

data.insert(1,'jamaik')
print('data sesudah di tambah =', data)

#menambahkan item di akhir
data.append('jujung')
print('penambahan data',data)

#menggabungkan data
new_data = ['juki','joseph','jonathan']
data.extend(new_data)
print('data gabungan =',data)

#merubah data
data[2] = 'joko'
print('data berubah',data)

#menghapus data
data.remove('asep')
print('data =',data)

#menghapus data terakhir
data_akhir = data.pop()
print('data akhir =',data)

print(data_akhir)