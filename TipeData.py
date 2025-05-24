#a = 10, a adalah variable dengan nilai 10

#tipe data integer (angka satuan)
data_integer = 5
print("data : ", data_integer, ", bertipe :", type(data_integer))

#tipe data float (desimal)
data_float = 5.4    #koma = .
print("data : ", data_float, ", bertipe :", type(data_float))

#tipe data string (kumpulan karakter)
data_string = "asep 5"
print("data : ", data_string, ", bertipe :", type(data_string))

#tipe data boolean (binner true/false)
data_bool = False
print("data : ", data_bool, ", bertipe : ", type(data_bool))

print("~~~~Mengubah Tipe Data~~~~")

print("======INTEGER======")#####
data_int = 9
print("data =", data_int, "type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print("data =", data_float, "type =",type(data_float))
print("data =", data_str, "type =",type(data_str))
print("data =", data_bool, "type =",type(data_bool))

print("======FLOAT=====")
data_float = 9.5
print("data =", data_float, "type =",type(data_float))

data_int   = int(data_float)  #dibulatkan ke bawah
data_str   = str(data_int)
data_bool  = bool(data_int) #0 false
print("data =", data_int, "type =",type(data_int))
print("data =", data_str, "type =",type(data_str))
print("data =", data_bool, "type =",type(data_bool))

print("======STRING=====")
data_str = 90;
print("data =", data_str, "type =",type(data_str))

data_int   = int(data_str)
data_float = float(data_str)
data_bool  = bool(data_str)
print("data =", data_int, "type =",type(data_int))
print("data =", data_float, "type =",type(data_float))
print("data =", data_bool, "type =",type(data_bool))

print("======BOLEAN=====")
data_bool = 9;
print("data =", data_bool, "type =",type(data_bool))

data_int   = int(data_bool)
data_float = float(data_bool)
data_str   = str(data_bool)
print("data =", data_int, "type =",type(data_int))
print("data =", data_float, "type =",type(data_float))
print("data =", data_str, "type =",type(data_str))
