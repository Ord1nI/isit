import matplotlib.pyplot as plt
import math
print("ВТОРАЯ РАБОТА")
f2_x = []
x2 = []
table_data2 = []


x = 3.45
y = 2.0
s = 0
for k in range(1,11):
    s = s + (math.e**x/k + math.e**-x/k/((x-1)**2 + (y-1)**2 + k**2)**1/4)
    for i in range(1,5):
        s = s + math.asin(1/x)-y**-k/(abs(k+k+y))**1/3
    f2_x.append(s)
    x2.append(k)
    table_data2.append([k,'%.3f' % s])
    print('%.3f' % s)

plt.title('График функции y=.....', fontsize=16, fontname='Times New Roman')
plt.scatter(x2, f2_x,
           c = 'red', marker='*')
plt.grid('on')
plt.plot(x2, f2_x, c = 'green')
plt.figure('Таблица',)
plt.title('Таблица значений функции y=.....', fontsize=20, fontname='Times New Roman')
plt.table(cellText=table_data2, loc='center', colLabels = ['x', 'y'])
plt.axis('off')
plt.show()