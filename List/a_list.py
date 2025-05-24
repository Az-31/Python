#kumpulan data

data_angka = [1,2,3,4,5]
print(data_angka)

data_string = ['cireng','martabak','ayam']
print(data_string)

data_boolean = [True, False, False, True]
print(data_boolean)


data_range = range(0,10,2) #start, stop, step
print(data_range)
data_list = list(data_range)
print(data_list)

#for loop
list_for = [i for i in range (0,10)]
print(list_for)

#for loop with if
list_for_if = [i**2 for i in range(0,10) if i != 5] #if 5
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 == 0] #genap
print(list_for_if)

list_for_if = [i for i in range(0,10) if i%2 != 0] #ganjil
print(list_for_if)
