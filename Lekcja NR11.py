import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#Seaborn
#Wykres Liniowy
sns.set(rc={'figure.figsize': (8,8)})
sns.lineplot(x=[1,2,3,4],y=[1,4,9,16],
             label='linia nr1',color= 'red',
             marker='o',linestyle=':')
sns.lineplot(x=[1,2,3,4],y=[2,5,10,17],
             label='linia nr2',color='blue',
             marker='^',linestyle=':')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Wykres liniowy')
plt.show()
#wykres liniowy randomowe liczby(inny sposób)
s = pd.Series(np.random.randn(1000))
s = s.cumsum()
sns.set()

wykres = sns.relplot(kind='line',data=s,label='linia')
wykres.fig.set_size_inches(8,6)
wykres.fig.suptitle('Wykres losowych danych')
wykres.set_xlabels('indeksy')
wykres.set_ylabels('wartości')
wykres.add_legend()
#wykres.figure.subplots_adjust(left=0.1,right=0.9,
#                              bottom=0.1,top=0.9)
plt.show()


#Trzeci wykres liniowy(plik z bazy iris.csv)
sns.set()
df = pd.read_csv('iris.csv',header=0,sep=',',decimal='.')
print(df)
wykres = sns.lineplot(data=df,x=df.index,y='sepal lenght',
                      hue='class',palette=['red','green','blue'])
wykres.set_xlabel=('indeksy')
wykres.set_title=('Wykres liniowy z bazy danych iris')
wykres.legend(title='Rodzaj kwiatu')
plt.show()
#Wykre punktowy (randomowe liczby)
sns.set()
data = {'a': np.arange(10),
        'c': np.random.randint(0,50,10),
        'd': np.random.randn((10))}
data['b']= data['a'] + 10 *np.random.randn(10)
data['d']= np.abs(data['d'])*100
print(data['c'])
print(data['d'])
df= pd.DataFrame(data)
plot = sns.relplot(data=df,x='a',y='b',
                   hue='c',palette='bright',size='d',legend = True)
plot.fig.set_size_inches(6,6)
plot.set(xticks=data['a'])
plt.show()
#Wykres kolumnowy (I sposób)
data = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
        'Stolica':['Bruksela','New Dalhi','Brasilia','Warszawa'],
        'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],
        'Populacja':[111111198,1303171035,207846528,38675467]}
df= pd.DataFrame(data)
sns.set()
plot = sns.catplot(data=df,x='Kontynent',y='Populacja',
                   kind='bar',ci=None,hue='Kontynent',estimator=np.sum,
                   dodge=False,palette=['red','green','yellow'],
                   legend_out=False)
plot.fig.set_size_inches(7,6)
plot.add_legend(title='Populacja na kontynentach',loc='center')
plot.fig.suptitle('Populacja na kontynentach')
plt.show()
#Wykres kolunowy(II sobsób)
data = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
        'Stolica':['Bruksela','New Dalhi','Brasilia','Warszawa'],
        'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],
        'Populacja':[111111198,1303171035,207846528,38675467]}
df= pd.DataFrame(data)
sns.set()
plot=sns.barplot(data=df,x='Kontynent',y='Populacja',ci=None,
                 hue='Kontynent',estimator=np.sum,
                 dodge=False,palette=['red','green','yellow'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')
plt.show()
#wykres kolumnowy (III sposób)
data = {'Kraj':['Belgia','Indie','Brazylia','Polska'],
        'Stolica':['Bruksela','New Dalhi','Brasilia','Warszawa'],
        'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],
        'Populacja':[111111198,1303171035,207846528,38675467]}
df= pd.DataFrame(data)
print(df)
grupa= df.groupby('Kontynent')
etykiety= list(grupa.groups.keys())
wartosci= list(grupa.agg('Populacja').sum())
plt.bar(x=etykiety,height=wartosci,color=['yellow','green','red'])
plt.xlabel('Kontynent')
plt.ylabel('Populacja w mld')
plt.show()
