from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
def error():
    msg=messagebox.showinfo( "Ошибка", 'Массив введен неверно')
def count():
    inp = e1.get() 
    inp = inp.split(' ')
    y = 'массив:\n'
    sr = 0
    for i in inp: 
        if i.replace('.', '', 1).isdigit() :
            sr+=float(i)
        else:
            error()
            return
    sr = sr / len(inp)
    for i in inp:
        if abs(float(i)) <= sr:
            y+=i+'\n' 
    msg=messagebox.showinfo( "Ответ", y)

window = Tk()
window.title("Окно")
window.geometry("900x600")
window.config(bg = 'lightgray')

image = Image.open("Задание.png")
photo = ImageTk.PhotoImage(image)
lbl1 = Label(window, image=photo)
lbl1.place(x=70,y=0)
 
lbl2 = Label(window, text = 'Введите массив')
lbl2.place(x=50, y=200)
 
e1 = Entry(window, width=100)
b1 = Button(text="Проверить массив", width=15, height=3, command=count)

b1.place(x=300, y=225)
e1.place(x=150, y=200)


window.mainloop()


