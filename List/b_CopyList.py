# duplikat list

a = ['yuno','kazuma','violet']
print('a =',a)

b = a
print('b =',b)

# merubah member a / b
a[1] = 'kafka'
b.sort()
print('a =',a)
print('b =',b) #akan merubah kedua list

# duplikat list with copy
print('list c dengan a.copy()')
c = a.copy()

print('c =',c)

print('ubah data 1')
c[1] = 'yukino'

print('a =',a)
print('b =',b)
print('c =',c)
