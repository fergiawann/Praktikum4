# Latihan1 
x = int(input("masukan bilangan pertama: "))
y = int(input("masukan bilangan kedua: "))
if x > y:
    print("bilangan terbesar= ", x)
else:
    print("bilangan terbesar= ", y)

# Latihan2
a = int(input("bilangan ke 1- "))
b = int(input("bilangan ke 2- "))
c = int(input("bilangan ke 3- "))
if a < b:
    if b < c:
        print("urutan bilangan : ", a, c, b)
    else:
        print("urutan bilangan: ", c, b, c)
else:
    if a < c:
        print("urutan bilangan: ", b, a, c)
    else:
        if b < c:
            print("urutan bilangan: ", b, c, a)
        else:
            print("urutan bilangan: ", c, b, a)
