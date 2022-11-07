# Latihan3
for i in range(0, 10):
    for j in range(0, 10):
        product = i+j
        print(f"{product:>3}", end='')
    print()
print("FERGIAWAN SATRIO BAGASKORO")

# Latihan4
import random
n = int(input("masukan nilai N: "))
for i in range(n):
    a = random.uniform(0.0, 0.5)
    print("data ke: ", i+1, "=> ", a)
print("FERGIAWAN SATRIO BAGASKORO")