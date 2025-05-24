#Converter suhu


#program celcius ke isekai

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukkan suhu dalam celsius : '))
print("suhu adalah",celcius, "Celsius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur, "Reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")


#program reamur ke isekai
print("\nPROGRAM KONVERSI TEMPERATUR\n")

reamur = float(input('masukkan suhu dalam reamur : '))
print("suhu adalah",reamur, "Reamur")

#celcisus
reamur = (5/4) * reamur
print("suhu dalam celcius adalah",celcius, "Celcius")

#fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

#kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")


#program fahrenheit ke isekai
print("\nPROGRAM KONVERSI TEMPERATUR\n")

fahrenheit = float(input('masukkan suhu dalam fahrenheit : '))
print("suhu adalah",fahrenheit, "Fahrenheit")

#celcius
celcius = ((5/9) * fahrenheit) - 32
print("suhu dalam celcius adalah",celcius, "Celcius")

#reamur
reamur = ((4/9) * fahrenheit) -32
print("suhu dalam reamur adalah",reamur, "Reamur")

#kelvin
kelvin = ((5/9) * fahrenheit) - 32 + 273
print("suhu dalam kelvin adalah",kelvin, "Kelvin")


#kelvin ke isekai
print("\nPROGRAM KONVERSI TEMPERATUR\n")

kelvin = float(input('masukkan suhu dalam kelvin : '))
print("suhu adalah",kelvin, "Kelvin")

#celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah",celcius, "Celcius")

#fahrenheit
fahrenheit = ((9/5) * kelvin - 273) + 32
print("suhu dalam fahrenheit adalah",fahrenheit, "Fahrenheit")

#reamur
reamur = ((4/5) * kelvin) - 273
print("suhu dalam reamur adalah",reamur, "Reamur")