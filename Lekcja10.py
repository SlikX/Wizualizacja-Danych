import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

#bardzo prosty wykres liniowy
plt.plot([1,2,3,4])
plt.ylabel('Kox Liczby')
plt.show()

#Zmiana typu wykresu, kolor(ogólnie wygląd)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
plt.axis([0, 6, 0, 20])
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
plt.axis([0, 6, 0, 20])
plt.show()

#wiele wykresów na jednym płótnie
x = np.arange(0.,5.,0.2)
plt.plot(x, x, 'r--', x, x**2, 'bs', x, x**3, 'g^')
plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
plt.show()
#Wiele wykresów na jendym płótnie(pojednyńcze wywołanie)
a = np.linspace(0,2,100)
plt.plot(a, a, label="liniowa")
plt.plot(a, a**2, label="kwadratowa")
plt.plot(a, a**3, label="sześcienna")
plt.show()
#etykiety osi
plt.xlabel('etykieta x')
plt.ylabel("etykieta y")
#tytuł wykresu
plt.title("Prosty wykres")
#włączamy pokazanie legendy
plt.legend()
#Zapisywanie Pliku w postaci PNG, potem konwersja na jpg
plt.savefig('wykres matplot.png')
im1 = Image.open('wykres matplot.png')
im1 = im1.convert('RGB')
im1.save('nowy.jpg')
#Tworzenie wykresu sinusa
x = np.arange(0, 10, 0.1)
s = np.sin(x)
plt.plot(x, s, label="sin(x)")
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x)')
plt.legend()
plt.show()
