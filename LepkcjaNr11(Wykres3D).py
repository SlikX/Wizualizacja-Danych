import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data

#matlib 3d wykres liniowy
fig = plt.figure()
ax = fig.add_subplot(111,projection= '3d')
print(type(ax))
t= np.linspace(0,2*np.pi,100)
z = t
x = np.sin(t)*np.cos(t)
y = np.tan(t)
ax.plot(x,y,z, label='Zadanie 1')
ax.legend()
plt.show()

#matlib 3d wykres punktowy
np.random.seed(19600001)
def randrange(n,vmin,vmax):
    return(vmax-vmin)*np.random.rand(n)+vmin
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
n=100
for c,m,zlow,zhigh in [('r','o',-50,-25),('b','^',-30,-5)]:
    xs= randrange(n,23,32)
    ys = randrange(n,0,100)
    zs = randrange(n,zlow,zhigh)
    ax.scatter(xs,ys,zs,c=c,marker = m)
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
plt.show()
#wywołanie dwóch wykresów na jednym płótnie

fig = plt.figure(figsize=plt.figaspect(0.5))

ax = fig.add_subplot(1,2,1,projection='3d')
np.random.seed(19600001)
def randrange(n,vmin,vmax):
    return(vmax-vmin)*np.random.rand(n)+vmin

#ax = fig.add_subplot(111,projection='3d')
n=100
for c,m,zlow,zhigh in [('r','o',-50,-25),('b','^',-30,-5)]:
    xs= randrange(n,23,32)
    ys = randrange(n,0,100)
    zs = randrange(n,zlow,zhigh)
    ax.scatter(xs,ys,zs,c=c,marker = m)
ax.set_xlabel('X label')
ax.set_ylabel('Y label')

ax = fig.add_subplot(1,2,2,projection = '3d')
X,Y,Z = get_test_data()
ax.plot_wireframe(X,Y,Z,rstride=10,cstride=10)
plt.show()
