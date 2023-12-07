import tkinter as tk
import math as m
from tkinter import messagebox
from PIL import Image,ImageTk
def error(error_message):
    messagebox.showerror( "Ошибка",error_message) 
def clear_all():
    for i in range(3):
        dota[i].delete('0',tk.END)
        dotb[i].delete('0',tk.END)
        dotc[i].delete('0',tk.END)

def is_float(num):
    try:
        float(num)
    except:
        error("Некорректные данные")
        return(False)
    return(True)
def default_val():
    a = [0.85,-0.9,2.8]
    b = [2.1,3.3,-0.25]
    c = [3.1,4.0,4.5]
    for i in range(3):
        dota[i].insert(0,str(a[i]))
        dotb[i].insert(0,str(b[i]))
        dotc[i].insert(0,str(c[i]))
def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)**1/2
    

def get_all():
    a=[]
    b=[]
    c=[]
    arr=[]
    for i in range(3):
        if is_float(dota[i].get()) and is_float(dotb[i].get()) and is_float(dotc[i].get()):
            a.append(float(dota[i].get()))
            b.append(float(dotb[i].get()))
            c.append(float(dotc[i].get()))
        else:
            return(False)
    arr.append(a)
    arr.append(b)
    arr.append(c)
    return(arr)

def count():
    if get_all() == False:
        return
    arr = get_all()
    a = arr[0]
    b = arr[1]
    c = arr[2]
    distance = []
    distance.append(dist(a,b))
    distance.append(dist(a,c))
    distance.append(dist(b,c))
    min = distance[1]
    index = 0
    for i in range(1,3):
        if distance[i] < min:
            min = distance[i]
            index = i
    messagebox.showinfo('Ответ','Кратчайшее растояние между точками '+['A B','A C','B C'][index]+' = '+format(min,'.3f'))

window = tk.Tk()
window.title("title")
window.geometry("821x500")
window.config(bg='lightgrey')

image = Image.open('5/Задание.jpg')
photo = ImageTk.PhotoImage(image)
lbl1 = tk.Label(window, image=photo)

##точка a
dota = []
dotb = []
dotc = []
labelsa = []
labelsb = []
labelsc = []
for i in 'XYZ':
    dota.append(tk.Entry(width=20))
    dotb.append(tk.Entry(width=20))
    dotc.append(tk.Entry(width=20))
for i in 'XYZ':
    labelsa.append(tk.Label(window, text=i+'=',font="arial"))
    labelsb.append(tk.Label(window, text=i+'=',font="arial"))
    labelsc.append(tk.Label(window, text=i+'=',font="arial"))
lbla = tk.Label(window, text="A",font="arial")
lblb = tk.Label(window, text="B",font="arial")
lblc = tk.Label(window, text="C",font="arial")

button_count = tk.Button(text='Найти минимальное расстояние',command=count,bg='lightgreen')
button_clear = tk.Button(text='Очистить ввод',command=clear_all,bg='red')
button_standard = tk.Button(text='Заполнить точки стандартными значениями',command=default_val,bg='lightgreen')

lbl1.grid(row=1,columnspan=10)

lbla.grid(row=2,column=4)
lblb.grid(row=4,column=4)
lblc.grid(row=6,column=4)
for i in range(3):
    labelsa[i].grid(row=3,column=[1,3,5][i])
    labelsb[i].grid(row=5,column=[1,3,5][i])
    labelsc[i].grid(row=7,column=[1,3,5][i])
for i in range(3):
    dota[i].grid(row=3,column=[2,4,6][i])
    dotb[i].grid(row=5,column=[2,4,6][i])
    dotc[i].grid(row=7,column=[2,4,6][i])
button_count.grid(row=8,column=4)
button_standard.grid(row=9,column=4)
button_clear.grid(row=10,column=4)

window.mainloop()