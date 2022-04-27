import pandas as pd
import matplotlib.pyplot as plt
#Zad 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df.to_string())
#print(df)
dff = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
grupa = df.groupby('Rok').agg({'Liczba' : ['sum']})
grupa.plot(kind='line')
plt.legend()
plt.show()
#Zad 2
grupka = df.groupby('Plec').agg({'Liczba' : ['sum']})

grupka.plot(kind='bar', title='Liczba Urodzen(Mln)')
plt.legend(loc='center')
plt.show()
#Zad 3
grupeczka = df[df['Rok'] > 2012].groupby('Rok').agg({'Liczba' : ['sum']})

grupeczka.plot(kind='pie', subplots=True, autopct='%.2f %%',
           colors=['red', 'purple','green','blue','brown'])
plt.legend(loc='center')
plt.show()
#Zad4
grupson = dff.groupby('Sprzedawca').agg({'idZamowienia': ['count']})
grupson.plot(kind='bar')
plt.show()
