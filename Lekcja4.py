import litery
plik = open('tekst.txt','r')
#Wczytanie 10 znaków
znak = plik.read(10)
#wczytanie lini
wiersz = plik.readline()
#wczytanie reszty pliku
linie = plik.readlines()
#zamknięcie pliku
plik.close()

print(znak)
print(wiersz)
print(linie)

#SYS i tworzenie plików .txt bezpośrednio w python
import sys

print('Podaj kierunek studiów, rok i specjalizacje')
dane = sys.stdin.readline()

plik = open('dane.txt','w+')
plik.write(dane)
plik.close()

lista=[]
for a in range(7):
    lista.append(a)

plik = open('dane.txt','a+')
plik.writelines(str(lista))
plik.close()
#open with
with open('tekst.txt','r') as plik:
    for linia in plik:
        print(linia,end='')
#tworzenie klass
class PierwszaKlasa:
    """Pierwsza klasa python"""
    atrybut = 54321
    def pierwsza_metoda(self):
        return 'pierwsza metoda w klasie'

obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
print(obiekt.pierwsza_metoda())
obiekt.tekst = 'aaaa'
print(obiekt.tekst)
#Klasa razem z def
class Ksztalty:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.opis = 'To będzie klasa dla ogólnych kształtów'
    def pole(self):
        return self.x * self.y
    def obwow(self):
        return 2 * self.x + 2 * self.y
    def dodaj_opis(self,text):
        self.opis = text
    def skalowanie(self,czynnik):
        self.x = self.x * czynnik
        self.y = self.y * czynnik
prostokat = Ksztalty(10,30)
print(prostokat.pole())
print(prostokat.obwow())
prostokat.dodaj_opis('Prostokąt :)')
print(prostokat.opis)
prostokat.skalowanie(0.5)
print(prostokat.x)
print(prostokat.y)
