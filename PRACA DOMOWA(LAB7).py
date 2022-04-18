import numpy as np

#Zad 1
a = np.arange(3)
b = np.arange(3)
print(a*b)
#Zad 2
M1 = np.arange(9).reshape(3,3)
M2 = np.arange(16).reshape(4,4)
print(M1)
print(M1.min(axis = 0))
print(M1.min(axis = 1))
print(M2)
print(M2.min(axis = 0))
print(M2.min(axis = 1))
#Zad 3
a = np.arange(3)
b = np.arange(3)
c = a.dot(b)
print(c)
#Zad 4
Macierz1 = np.array([2, 4, 5, 6, 9])
Macierz2 = np.array([2.5, 3, 1.5, 0.2, 1.5])
print(Macierz1*Macierz2)
#Zad 5
Mac = np.arange(6).reshape(2,3)
a = np.sin(Mac)
print(a)
#Zad 6
Mac2 = np.arange(6).reshape(2,3)
b = np.cos(Mac2)
print(b)
#Zad 7
print(a+b)
#Zad 8 
KoxMacierz = np.arange(9).reshape(3,3)
for x in KoxMacierz:
    print(x)
#Zad 9
KolejnaMacierz = np.arange(9).reshape(3,3)
for x in KolejnaMacierz.flat:
    print(x)
#Zad 10
