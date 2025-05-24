###setiap hasil dari opresi komparasi adalah boolean

####  >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# LEBIH BESAR DARI
print('~~~~~~~~~~~~~~Lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(a,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# KURANG DARI
print('~~~~~~~~~~~~~~Kurang dari (<)')
hasil = a < 3
print(a, '<',3,'=',hasil)
hasil = b < 3
print(a, '<',3,'=',hasil)
hasil = b < 2
print(b, '<',2,'=',hasil)

# LEBIH BESAR SAMA DENGAN
print('~~~~~~~~~~~~~~Lebih besar sama dengan (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b > 3
print(a,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# LEBIH KECIL SAMA DENGAN
print('~~~~~~~~~~~~~~Lebih besar dari (=<)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# SAMA DENGAN
print('~~~~~~~~~~~~~~Sama dengan (==)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# TIDAK SAMA DENGAN
print('~~~~~~~~~~~~~~Tidak sama dengan (!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparaso object identity
print('~~~~~~~~~~~~~~ (is)')
x = 5
y = 5
z = 6
hasil = x is y
print('x is y =',hasil)
hasil = x is z
print('x is z =',hasil)

print('~~~~~~~~~~~~~~ (is not)')
hasil = x is not y
print('x is not y =',hasil)
hasil = x is not z
print('x is not z =',hasil)


