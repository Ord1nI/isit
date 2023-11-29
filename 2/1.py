import matplotlib.pyplot as plt
import numpy as np
import math
print("через цыкл for")
X = []
f_x = []
table_data = []

a = 1.35

for x in np.arange(-2,5,0.5):
    X.append(x)
    r = 0
    if x <=0.1:
        r = (x+2)**1/3+math.sin(x)**2
    if 0.1 < x < 2:
        r = a*x/x**2+0.32
    else: 
        r = math.atan((a*x/2)**2)
    print('%.3f' % r)
    f_x.append(r)
    table_data.append([x,'%.3f' % r])
plt.title('График функции y=.....', fontsize=16, fontname='Times New Roman')
plt.scatter(X, f_x,
           c = 'red', marker='*')
plt.grid('on')
plt.plot(X, f_x, c = 'green')
plt.figure('Таблица',)
plt.title('Таблица значений функции y=.....', fontsize=20, fontname='Times New Roman')
plt.table(cellText=table_data, loc='center', colLabels = ['x', 'y'])
plt.axis('off')
plt.show()
print("Через цыкл while")

x = -2.0
X = []
f_x = []
table_data = []
while(x <= 4):
    X.append(x)
    r = 0
    if x <=0.1:
        r = (x+2)**1/3+math.sin(x)**2
    if 0.1 < x < 2:
        r = a*x/x**2+0.32
    else: 
        r = math.atan((a*x/2)**2)
    print('%.3f' % r)
    f_x.append(r)
    table_data.append([x,'%.3f' % r])
    x+=0.5
plt.title('График функции y=.....', fontsize=16, fontname='Times New Roman')
plt.scatter(X, f_x,
           c = 'red', marker='*')
plt.grid('on')
plt.plot(X, f_x, c = 'green')
plt.figure('Таблица',)
plt.title('Таблица значений функции y=.....', fontsize=20, fontname='Times New Roman')
plt.table(cellText=table_data, loc='center', colLabels = ['x', 'y'])
plt.axis('off')
plt.show()