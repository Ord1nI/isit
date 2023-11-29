from tkinter import *
from PIL import Image,ImageTk
window = Tk()
window.title("Зимин Дмитрий АС 22-05")
window.geometry("1920x1080")

image = Image.open('Задание.png')
photo = ImageTk.PhotoImage(image)
lbl1 = Label(window, image=photo)
lbl1.grid(column=0, row=0, sticky='W')

X = [0.34, 99.2, 52.3, 0.5, 1, 2.23, -15.9, 10.2, 0, -3.9]
text1 = "X = " + str(X) + " - заданный массив"
print(text1)
lbl2 = Label(window, text=text1, font="Arial 14")
lbl2.grid(column=0, row=1, sticky='W')
ysl = 'x<=p, где p- сумма нечётных элементов массива Х'
ysl1 = Label(window, text=ysl, font='Arial 10')
ysl1.grid(column=0, row=2, sticky='W')
p = 0
Y = []
for i in range(10):
    if i % 2 == 0:
        p += X[i]
for i in range(10):
    if X[i] <= p:
        Y.append(X[i])
ysl = 'p='+ str(p)
ysl2 = Label(window, text=ysl, font='Arial 10')
ysl2.grid(column=0, row=3, sticky='W')
if len(Y) == 0:
    print('Искомых элементов нет')
    text2 = 'Искомых элементов нет'
    lbl3 = Label(window, text=text2, font="Arial 14")
    lbl3.grid(column=0, row=4, sticky='W')
else:
    print(Y)
    text2 = "Y = " + str(list(float("{0:.4f}".format(i)) for i in Y)) + " - полученный массив"
    lbl3 = Label(window, text=text2, font="Arial 14")
    lbl3.grid(column=0, row=4, sticky='W')
window.mainloop()
