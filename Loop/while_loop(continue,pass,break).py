#while
angka = 0

while angka < 5:
    angka +=1
    print(angka)

print('=====')

#continue

bilangan = 0

print('bilangan ini', bilangan)

while bilangan < 5:
    bilangan +=1
    print('-', bilangan)

    if bilangan == 3:
        print('oi oi oi')
        continue  #semua looping akan di skip

    print('coy')

print('=continue=')

#pass

bilangan_1 = 0

print('bilangan ini', bilangan_1)

while bilangan_1 < 5:
    bilangan_1 +=1
    print('-', bilangan_1)

    if bilangan_1 == 3:
        print('oi oi oi')
        pass  #tidak akan dieksekusi

    print('coy')

print('=pass=')

#break

bilangan_2 = 0

while bilangan_2 < 5:
    bilangan_2 +=1
    print('-', bilangan_2)

    if bilangan_2 == 3:
        print('oi oi oi')
        break  #stop

    print('coy')

print('=break=')


#contoh program
data = int(input('Angka = '))

bilangan_3 = 0

while True:
    bilangan_3 +=1
    print('angka = ', bilangan_3)

    if bilangan_3 == data:
        print('oi oi oi')
        break  #stop

    print('coy')