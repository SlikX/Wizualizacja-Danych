#Zad 1 ulubione sporty
from typing import List
import math

lista1 = ["siatkowka","MMA", "pilka nozna"]
lista1.reverse()
lista1.append("zuzel")
lista1.append("boks")
print(lista1)
#Zad 2 Slownik gazeta
slownik = {'FAQ': 'Frequenly Asked Questions', 'DIY': 'Do It Yourself', 'BTW': 'But The Way'}
print(slownik)
#Zad 3 slownik gier
slownik1 = {'LoL': 'League Of Legends', 'WoW': 'World of Warcraft', 'Souls': 'Dark souls 1/2/3'}
print(len(slownik1))
#Zad 4 Poberanie zdania i liczenie slowa a
x = input()
print(x.count('a'))
#Zad 5 a do potęgi plus c
a = int(input("liczbaPierwsza: "))
b = int(input("liczbaDruga: "))
c = int(input("liczbaTrzecia: "))
print(pow(a,b)+c)
# zad 6 która największa liczba if else
x = int(input("X: "))
y = int(input("Y: "))
z = int(input("Z: "))
if (x > y and x > z):
    print('liczba X jest najwieksza')
elif (y > x and y > z):
    print('liczba Y jest najwieksza')
else:
    print('liczba Z jest najwieksza')

