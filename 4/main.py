import tkinter as tk
import math as m
from tkinter import messagebox
from PIL import Image,ImageTk
def to_float(num):
    try:
        float(num)
    except:
        error("Некорректный ввод")
        return(False)
    return(True) 
def clear():
    e1.delete(0, 'end') 
def error(error_message):
    messagebox.showerror( "Ошибка",error_message) 
def count():
    b = e1.get()
    if to_float(b):
        b = float(b)
    if b > 10 or b < 0:
        error('Некорректное b')
        return
    print(b>0)
    output = ''
    arr = []
    for i in range(5):
        a = []
        for j in range(5):
            if i>2:
                a.append(i*i + (i-j**b)**1/2)
                output += format(a[j],'.3f') + '  '
            if i<=2:
                a.append((b-0.375)*((b-i)/(j+5/1+(1+j))))
                output += format(a[j],'.3f') + '  '
        arr.append(a)
        output += '\n'
    messagebox.showinfo( "Ответ", output)
    print(arr)
    print(output)


        
        
window = tk.Tk()
window.title("Задание 4")
window.geometry("1920x1080")

image = Image.open('задание(1).png')
photo = ImageTk.PhotoImage(image)
lbl1 = tk.Label(window, image=photo)
lbl1.place(x=70,y=0)
lbl2 = tk.Label(window,text='Введите b(b<=10,b>=0)')


e1 = tk.Entry(window, width=100, background='lightblue')
b1 = tk.Button(text="Проверить массив", width=15, height=3, command=count, background='lightgreen')

bclear = tk.Button(text="Очистить ввод", width=15, height=3, command=clear, background='indianred')
lbl2.place(x=400,y=230)
b1.place(x=386, y=285)
e1.place(x=150, y=260)
bclear.place(x=386, y=360)
window.mainloop()
