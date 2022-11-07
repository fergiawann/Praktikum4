# Latihan5
x = int(input("masukan bilangan pertama: "))
y = int(input("masukan bilangan kedua: "))
z = int(input("masukan bilangan ketiga: "))
if x > y:
    if x > z:
        print("\nBilangan terbesar= ", x)
    elif y > z:
        print("\nBilangan terbesar= ", y)
    else:
        print("\nBilangan terbesar= ", z)