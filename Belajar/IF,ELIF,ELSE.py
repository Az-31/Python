
print(10*"=")
print("KALKULATOR")
print(10*"=")

angka_1 = float(input("Masukkan angka ke-1 :"))
operator = input('+,-,x,/ :')
angka_2 = float(input('Masukkan angka ke-2 :'))

if operator == '+':
    hasil = angka_1 + angka_2
    print(f'Hasil adalah ={hasil}')
elif operator == '-':
 
   hasil = angka_1 - angka_2
   print(f'Hasil adalah ={hasil}')
elif operator == 'x':
   hasil = angka_1 * angka_2
   print(f'Hasil adalah ={hasil}')
elif operator == '/':
   hasil = angka_1 / angka_2
   print(f'Hasil adalah ={hasil}')
else :
   print("Hahh??")
