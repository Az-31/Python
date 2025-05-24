# list bersarang 

data_0 = [1,2]
data_1 = [3,2]

list_2d = [data_0,data_1]
print(list_2d)

# exm
print('='*130)
pers_0 = ['megumin',18,'perempuan']
pers_1 = ['yunyun',19,'onanoko']
pers_2 = ['satoru',24,'otoko']
pers_3 = ['giorno',16,'laki-laki']

list_pesr = [pers_0,pers_1,pers_2,pers_3]

print('peserta =',list_pesr)

for peserta in list_pesr:
    print('Nama :', peserta[0])
    print('Umur :', peserta[1])
    print(f'Sex  : {peserta[2]}\n')