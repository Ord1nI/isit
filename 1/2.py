import math as m
x = float(input('Введите x: '))
y = float(input('Введите y: '))
a = 0.0
b = 0.0

if (m.sqrt(abs(x)) - m.sqrt(abs(y))):
    a = 4 - x**2 / (m.sqrt(abs(x)) - m.sqrt(abs(y)))
if (x**2 - y**2 > 0 and x > y):
    b = m.log(x**2 - y**2) + m.sqrt(abs(x/y))

if (a**2 + b**2 > 0 and x > y):
    print("%.3f" % float(m.sqrt(abs(a+b))))
elif (a**2 + b**2 <=1 and a**2 + b**2 != 0):
    print("%.3f" % float(a + b))
else:
    print("Ошибка")
    
