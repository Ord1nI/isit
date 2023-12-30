import tkinter as tk
from PIL import Image,ImageTk
from pprint import pprint
def convert_matrix_to_str(arr):
    m_str = ''
    for i in range(len(arr)):
        m_str1 = '['
        for q in range(len(arr[0])):
            m_str1 += "%.3f" % arr[i][q] + ' '
        m_str += m_str1 + ']\n'
    return m_str
def sort_vector(vector):
    for i in range(len(vector)):
        for q in range(i):
            if vector[i] < vector[q]:
                vector[i],vector[q] = vector[q],vector[i]
    return vector
def vect(arr):
    vector = []
    for i in range(9):
        vector.append(arr[i][i])
    return vector
def vect_to_str(vector):
        v = '['
        for i in range(len(vector)):
            v += '%.3f' % vector[i] + ' '
        v += ']'
        return v
def gen_matrix():
    b = 4
    arr = []
    result = ''
    for i in range(9):
        arr1 = []
        for j in range(9):
            if i <=3:
                ii =i+1
                jj= j+1
                arr1.append(round((b-0.375)*((b-ii/jj+5)/(1+(ii+jj))),4))
            if i > 3:
                ii = i+1
                jj = j+1
                arr1.append(round(ii*ii+(ii-jj**b)**1/2,4))
        arr.append(arr1)
    return arr
def sr(arr):
    sr = 0
    countel = 0
    for i in range(9):
        sr += arr[i][i]
    sr = sr/9
    for i in range(9):
        for q in range(9):
            if arr[i][q] > sr:
                countel+=1
    return sr, countel
def count():
    arr = gen_matrix()
    arr_changed = arr.copy()
    arr_changed[1],arr_changed[4] = arr_changed[4], arr_changed[1]
    sred, countel = sr(arr)
    vector = vect(arr)
    matrix_text.insert(0.0,convert_matrix_to_str(arr))
    matrix2_text.insert(0.0,convert_matrix_to_str(arr_changed))
    text_sr.insert(0.0,'%.3f' % sred)
    text_src.insert(0.0,countel)
    x_text.insert(0.0,vect_to_str(vector))
    x_sorted_text.insert(0.0,vect_to_str(sort_vector(vector)))
    

window = tk.Tk()
window.title("title")
window.geometry("1501x1000")
window.config(bg='lightgrey')
image = Image.open('Задание.PNG')
photo = ImageTk.PhotoImage(image)
lbl1 = tk.Label(window, image=photo)
btn1 = tk.Button(window,text="Выполнить",width=20,height=5,bg='lightgreen',command=count)
lblmatrix = tk.Label(text='матрица A')
matrix_text = tk.Text(height=9,width=90)
lblmatrix2= tk.Label(text='матрица A измененная')
matrix2_text = tk.Text(height=9,width=90)
lblsr = tk.Label(text='среднее занчение матрицы')
text_sr = tk.Text(height=1,width=10)
lblsrc = tk.Label(text='кол-во значений')
text_src = tk.Text(height=1,width=10)
lblx = tk.Label(text='вектор x')
x_text = tk.Text(height=1)
lblx_sorted = tk.Label(text='отсортированный массив')
x_sorted_text = tk.Text(height=1)



lbl1.pack()
btn1.pack()
lblmatrix.pack()
matrix_text.pack()
lblmatrix2.pack()
matrix2_text.pack()
lblsr.pack()
text_sr.pack()
lblsrc.pack()
text_src.pack()
lblx.pack()
x_text.pack()
lblx_sorted.pack()
x_sorted_text.pack()
window.mainloop()