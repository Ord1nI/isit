import tkinter as tk
import math
from tkinter import messagebox

win = tk.Tk()
win.config(cursor = 'dot red')
win.title('Лабораторная работа №3')
win.geometry('400x250')
win.config(bg = 'lightgray')
def geta():
    xx = float(namex.get())
    yy = float(namey.get())
    a = xx + yy
    vivodx.insert(0, '%8.4f' % a)
lbl1 = tk.Label(win, text = 'Введите x =')
lbl1.place(x = 60, y = 40)
lbl2 = tk.Label(win, text = 'Введите y =')
lbl2.place(x = 60, y = 85)
namex = tk.Entry(win, cursor = 'heart red', foreground = 'red', highlightcolor = 'red', background = 'lightblue')
namex.focus()
namex.place(x = 170, y = 40)
namey = tk.Entry(win, cursor = 'gumby yellow', foreground = 'blue')
namey.config(background = 'pink')
namey.place(x = 170, y = 85)
btn1 = tk.Button(win, text = 'Считаем A', command = geta, relief = tk.RAISED, cursor = 'sailboat blue blue')
btn1.place(x = 100, y = 190)
btn1.config(background = 'lightblue')
vivodx = tk.Entry(win, foreground = 'green', font = 'bold')
vivodx.place(x = 100, y = 150)
win.mainloop()
