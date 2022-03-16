#Podnoszenie do kwadratu
listaA = []
for x in range(0,10):
    listaA.append(x**2)
#print(listaA)
#X jako wykładnik
listaB = []
for x in range(0,6):
    listaB.append(3**x)
#print(listaB)
#Nieparzyste z listyA
listaC = []
for x in listaA:
    if(x % 2 != 0):
        listaC.append(x)
#print(listaC)
#Nieparzyste z listyA drugi sposób
ListaC2 = [x for x in listaA if(x%2 != 0)]
#print(ListaC2)



lista = []
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        lista.append((a, b))
    #print(lista)
    lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
    #print(lista2)


#odwórcenie klucza z warością
slownik = {'PZU ': 'Panstwowy zakład ubezpieczeń','ZUS ':'Zakład ubezpieczeń społecznych','PKO ':'Państwowa kasa oczszędności'}
print(slownik)
slownik_odwrocony = {}
for key, value in slownik.items():
    slownik_odwrocony[value] = key
print(slownik_odwrocony)
#odwórcenie klucza z warością  skórcona wersja
slownik2 = {value: key for key, value in slownik.items()}
print(slownik2)
#Równanie kwadratowe
import math
def row_kwadratowe (a,b,c):
    delta = b++2-4*a*c
    if delta < 0:
        print('Mniejsze wieksze')
        return -1
    elif delta == 0:
        x = (-b)/(2+a)
        return x
    else:
        x1= ((-b)- math.sqrt(delta))/(2*a)
        x2= ((-b)+ math.sqrt(delta))/(2*a)
        return x1,x2

print(row_kwadratowe(6,1,6))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))


#funkcja parzystośći
def parzy_Nieparzy (a):
    if  (a%2 == 0):
        return 'Liczba jest parzysta'
    else:
        return 'Liczba nieparzysta'
#frunkja długość odcinka
print(parzy_Nieparzy(3))
import math
def dlugosc_odcinka(x1=1,y1=2,x2=3,y2=4):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
#argumenty domyślne
print(dlugosc_odcinka())
#argumenty pozycyjne
print(dlugosc_odcinka(4,5,6,9))
#dwa pirwsze argumenty pozycyjne (kolejność bez znaczenia)
print(dlugosc_odcinka(1,1,y2=8,x2=7))
#funkcja ciąg gwiazdka wieczne przypisowywanie wartości dla argumenty funkcji
def ciag(*liczba):
    if len(liczba) == 0:
        return 0
    else:
        suma = 0
        for i in liczba:
            suma += i
        return suma
print(ciag())
print(ciag(1,2,3,4,5,6,7,8))
#funkcja przyjmująca argument z dwiema gwiazdkami
def co_lubie(** rzeczy):
    for cos in rzeczy:
        print("lubie ")
        print(cos)
        print('co lubie ')
        print(rzeczy[cos])
co_lubie(narkotyki=['kox'])
