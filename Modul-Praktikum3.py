# Latihan6
import random
n = int(input("masukan nilai N: "))
for i in range(n):
    a = random.uniform(0.0, 0.5)
    print("data ke: ", i+1, "=> ", a)
print("FERGIAWAN SATRIO BAGASKORO")

# Latihan7
n = 1
a = 0
while n !=0:

    if n > a:
        a = n
    n = int(input("masukan bilangan: "))

    if n == 0:
        break
print("nilai terbesarnya adalah: ", a)

# Latihan8
n = 100000000
sum = 0
y = 0
laba = [int(0), int(0), int(n) * 0.01, int(n) * 0.01, int(n) *
        0.05, int(n) * 0.05, int(n) * 0.05, int(n) * 0.03]
for i in laba:
    sum = sum+i
    y += 1
    print("laba bulan ke-", y, "sebesar: ", i)
print("total laba adalah: ", sum)