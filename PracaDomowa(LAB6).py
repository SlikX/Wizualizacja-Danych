#Zad 1
import numpy as np
a = np.arange(21)
print(4*a)
#Zad 2
b = np.arange(6, dtype=float)
print(b)
c = b.astype('int32')
print(c)
#Zad 3
def funkcja(n):
    kox=n*n
    k = np.arange(kox)
    print(pow(2,k))
n = input('Podaj liczbe: ')
n = int(n)
print(funkcja(n))
#Zad 4:
