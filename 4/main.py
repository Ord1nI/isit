import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
def clear():
    e1.delete(0, 'end') 
def error():
    messagebox.showinfo( "Ошибка", 'Некорректные данные')
def count():
    b = e1.get()
    try:
        float(b)
    except:
        error()
        return
    b = float(b)
    output = ''
    arr = []
    for i in range(5):
        a = []
        for j in range(5):
            if i>3:
                a.append(i*i+(i-j**b)**1/2)
                output += '%.3f' % a[j] + ' '
            if i<=3:
                a.append((b-0.375)*((b-i)/(j+5/1+(1+j))))
                output += '%.3f' % a[j] + ' '
        arr.append(a)
        output += '\n'
    messagebox.showinfo( "Ответ", output)
    print(output)


        
        
window = tk.Tk()
window.title("title")
window.geometry("1920x1080")

image = Image.open('задание(1).png')
photo = ImageTk.PhotoImage(image)
lbl1 = tk.Label(window, image=photo)
lbl1.place(x=70,y=0)


e1 = tk.Entry(window, width=100, background='lightblue')
b1 = tk.Button(text="Проверить массив", width=15, height=3, command=count, background='lightgreen')

bclear = tk.Button(text="Очистить ввод", width=15, height=3, command=clear, background='indianred')

b1.place(x=300, y=275)
e1.place(x=150, y=250)
bclear.place(x=300, y=350)
window.mainloop()
