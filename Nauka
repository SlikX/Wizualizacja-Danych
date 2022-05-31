WYKRES SŁÓPKOWY:
labels = list('ABCD')
values = np.random.randint(10, 30, 4)
variance = np.random.randint(1, 4, 4)

plt.bar(labels, values, color='purple')
plt.title('Bar chart')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()

#ZAPISYWANIE ZDJ
from PIL import Image
plt.savefig('wykres matplot.png')
im1 = Image.open('wykres matplot.png')
im1 = im1.convert('RGB')
im1.save('nowy.jpg')

WYKRES SKUMULOWANY
values_A = np.random.randint(10, 30, 4)
values_B = np.random.randint(10, 30, 4)

plt.bar(labels, values_A, label='values_A')
plt.bar(labels, values_B, label='values_B', bottom=values_A)
plt.legend()
plt.show()

WYKRES SKUMULOWANY PORÓWNYWANIE
width = 0.4
index = np.arange(len(labels))
plt.bar(index - width/2, values_A, width, label='values_A')
plt.bar(index + width/2, values_B, width, label='values_B')
plt.xticks(index, labels)
plt.legend()
plt.show()


#DWA WYKRESY JEDNO PŁÓTNO
x1 = np.arange(-4,5)
x2 = np.arange(-4,5)
y1 = 5*pow(x1,2)-3*x1+2
y2 = -2*pow(x2,3)+5
fig, axs = plt.subplots(2, 2 )
axs[0,1].plot(x1,y1,'r')
axs[1,0].plot(x2, y2, 'g')
#fig.delaxes(axs[1,0])
#fig.delaxes(axs[0,1])
plt.show()

#WYKRES PUNKTOWY
x_values = np.random.randint(20, 80, 20)
y_values = np.random.randint(30, 120, 20)
y2_values = np.random.randint(30, 120, 20)

plt.scatter(x_values, y_values)
plt.xlim(0, 100)
plt.ylim(0, 150)
plt.title('Scatter plot')
plt.show()

TWORZENIE DATAFRAME PROSTE

a = [['Ania',24],['Michał',9],['Darek',40],['Ewa',43]]
df_a = pd.DataFrame(a)
df_a.columns = 'Imię', 'Wiek'
df_a

TWORZENIE DATAFRAME NA BAZIE SŁOWNIKA
b = {'Imię':['Ewa','Michał','Krzysiek','Kasia','Lucja'],'Miasto':['Warszawa','Kraków','Gdańsk','Poznań','Łódź']}
df_b = pd.DataFrame(b)
df_b

CZYTANIE CSV
df = pd.read_csv('dane.csv', header=0, sep=";",decimal=',')
CZYTANIE EXCEL
import openpyxl
df = pd.read_excel(xlsx, header=0)
xlsx=pd.ExcelFile('dane.xlsx')
