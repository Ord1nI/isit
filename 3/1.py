from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
def clear():
    e1.delete(0, 'end') 
def error():
    msg=messagebox.showinfo( "Ошибка", 'Массив введен неверно')
def count():
    inp = e1.get() 
    inp = inp.split(' ')
    y = 'массив:\n'
    for i in inp: 
        if i.replace('.', '', 1).isdigit() :
            if float(i).is_integer():
                y+=i+'\n'
        else:
            error()
            return
    msg=messagebox.showinfo( "Ответ", y)

window = Tk()
window.title("Окно")
window.geometry("800x400")
window.config(bg = 'lightgray')

image = Image.open("Задание.png")
photo = ImageTk.PhotoImage(image)
lbl1 = Label(window, image=photo)
lbl1.place(x=70,y=0)
lbl2 = Label(window, text = 'Введите массив')
lbl2.place(x=50, y=200)
e1 = Entry(window, width=100, background='lightblue')
b1 = Button(text="Проверить массив", width=15, height=3, command=count, background='lightgreen')

bclear = Button(text="Очистить ввод", width=15, height=3, command=clear, background='indianred')

b1.place(x=300, y=225)
e1.place(x=150, y=200)
bclear.place(x=300, y=300)


window.mainloop()


