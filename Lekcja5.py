class Kształty():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.opis = "To jest klasa dla ogólnych kształtów"
    def pole(self):
        return self.x*self.y
    def obwod(self):
        return 2*self.x+2*self.y
    def opis(self,text):
        self.opis = text
    def skalowanie(self,czynnik):
        self.x *= czynnik
        self.y *= czynnik
class Kwadrat(Kształty):
    def __init__(self,x):
        self.x = x
        self.y = x
class KwadratAleToLiteraL(Kwadrat):
    def obwod(self):
        return 8 * self.x
    def pole(self):
        return 3*self.x*self.y
#inicjacja Kwadratu
kwadrat = Kwadrat(5)
print(kwadrat.obwod())
print(kwadrat.pole())
kwadrat.opis("Kozak kwadrat")
print(kwadrat.opis)
#Konkstruktor klasy bazowej i dziedziczenie wielokrotne
class osoba:
    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
    def przedstaw_sie(self):
        return "{} {}".format(self.imie,self.nazwisko)
class pracownik(osoba):
    def __init__(self,imie,nazwisko,pensja):
        #wywołanie poprzedniej klasy wow
        osoba.__init__(self,imie,nazwisko)
        self.pensja = pensja
    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie,self.nazwisko,self.pensja)
class menadzer(pracownik):
    def przedstaw_sie(self):
        return "{} {} jestem menadżerem i zarabiam {}".format(self.imie,self.nazwisko,self.pensja)
#nadawanie wartości
jozek = pracownik('Tomasz','Działowy',2000)
jakub = menadzer('Jakub','Karcz',20000000000000000000000000000)
#wywołanie
print(jozek.przedstaw_sie())
print(jakub.przedstaw_sie())
