import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)

grupa = df.groupby('Imię i nazwisko').agg(
        {'Wartość zamówienia': ['sum']})

grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
           fontsize=20, figsize=(8, 8), colors=['white', 'red'])
plt.legend(loc='upper left')
plt.show()
