#Zad 1
import random
X = random.randint(0,30)
X *= 2
plik = open("plik.txt",'a')
X=str(X)
plik.write(X)
plik.close()
#Zad 2
plik =open("plik.txt", "r")
print(plik.read())
plik.close()
#Zad 3
with open("plik.txt", "a") as text:
    text.write("Dodanytekst\n")
with open("plik.txt", "r") as text:
    for Dodanytekst in text:
        print(text.read())
#Zad 4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu=nazwa_produktu
        self.ilosc=ilosc
        self.jednostka_miary=jednostka_miary
        self.cena_jed=cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)
    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed
produkt=NaZakupy("Żelki", 20, "Szt", 0.5)
print(produkt.ile_kosztuje())
#Zad 5 Robson
class Robson:
    def __init__(self, x,y,kroki):
        self.x=x
        self.y=y
        self.krok=kroki
    def do_gory(self, a):
        self.y=self.y+(self.krok*a)
    def do_dolu(self, b):
        self.y=self.y-(self.krok*b)
    def lewo(self, c):
        self.x=self.x-(self.krok*c)
    def prawo(self, d):
        self.x=self.x+(self.krok*d)
    def gdzie_jest_Robson(self):
        print(self.x, self.y)
robak=Robson(0,0,2)
robak.do_dolu(20)
robak.do_gory(4)
robak.lewo(8)
robak.prawo(1)
print('Robson jest: ')
robak.gdzie_jest_Robson()
