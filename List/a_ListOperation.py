data_angka = [1,2,4,5,6,7,7,5,9,8,0,7,6,4,3]
print(data_angka)

# menentkan berapa bnyk data yg kluar(.count)
jumlah_data_7 = data_angka.count(7)
jumlah_data_1 = data_angka.count(1)

print('jumlah angka 7 =',jumlah_data_7)
print('jumlah angka 1 =',jumlah_data_1)

# mengambil index data
data_index = data_angka.index(8)
print('index 8 =',data_index)

# mengurutkan data
data_angka.sort()
print('data urut =',data_angka)

# invers list
data_angka.reverse()
print('data urut invers =',data_angka)