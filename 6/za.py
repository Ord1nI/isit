from PIL import Image,ImageTk
from pprint import pprint
import tkinter as tk
import random
def clear_all():
    matrix_text.delete(0.0,tk.END)
    min_text.delete(0.0,tk.END)
    max_text.delete(0.0,tk.END)
    vect_text.delete(0.0,tk.END)
    svect_text.delete(0.0,tk.END)
def convert_matrix_to_str(arr): 
    m_str = ''
    for i in range(len(arr)):
        m_str1 = '['
        for q in range(len(arr[0])):
            m_str1 += str(arr[i][q]) + ' '
        m_str += m_str1 + ']\n'
    return m_str
def vect_to_str(vector):
        v = '['
        for i in range(len(vector)):
            v +=  str(vector[i]) + ' '
        v += ']'
        return v
def gen_matrix():
    arr = []
    for i in range(6):
        arrm = []
        for q in range(6):
            arrm.append(random.randint(-100,100))
        arr.append(arrm)
    return(arr)
def gen_vector(vect,min_index,max_index):
    vect2 = []
    if min_index[0] > max_index[0]:
        min_index,max_index = max_index,min_index
    if min_index[0] == max_index[0] and min_index[1] > min_index[1]:
        min_index,max_index = max_index,min_index
    for i in range(min_index[2]+1,max_index[2]):
        vect2.append(vect[i])
    return(vect2)
def find_min_max(arr):
    vect = []
    min = 1000000
    max = 0
    min_index = [0,0,0]
    max_index = [0,0,0]
    count = 0
    for i in range(6):
        for q in range(0,i+1):
            vect.append(arr[i][q])
            if arr[i][q] < min:
                min = arr[i][q]
                min_index[0] = i
                min_index[1] = q
                min_index[2] = count
            if arr[i][q] > max:
                max = arr[i][q]
                max_index[0] = i
                max_index[1] = q
                max_index[2] = count
            count += 1
    return(min_index,max_index,vect)
def sort_vector(vect):
    sorted_vect = []
    for i in vect[1::2]:
        if i > 0:
            sorted_vect.append(i)
    for i in range(len(sorted_vect)):
        for q in range(i,len(sorted_vect)):
            if sorted_vect[i] < sorted_vect[q]:
                sorted_vect[i],sorted_vect[q] = sorted_vect[q],sorted_vect[i]
    return(sorted_vect)

def mainf():
    clear_all()
    arr = gen_matrix()
    arr_str = convert_matrix_to_str(arr)
    min_index,max_index,vect = find_min_max(arr)
    vect=gen_vector(vect,min_index,max_index)
    sorted_vect = sort_vector(vect)
    matrix_text.insert(0.0,arr_str)
    min_text.insert(0.0,str(min_index[0]+1) + ' ' + str(min_index[1]+1))
    max_text.insert(0.0,str(max_index[0]+1) + ' ' + str(max_index[1]+1))
    if not vect:
        vect_text.insert(0.0,'мин. и макс. элементы находятся рядом')
    else:
        vect_text.insert(0.0,vect_to_str(vect))
    if not sorted_vect:
        svect_text.insert(0.0,"Невозможно отсортировать")
    else:
        svect_text.insert(0.0,vect_to_str(sorted_vect))

    




window = tk.Tk()
window.title("title")
window.geometry("1501x1000")
window.config(bg='lightgrey')
btn1 = tk.Button(window,text="Выполнить",width=20,height=5,bg='lightgreen',command=mainf)
lblmatrix = tk.Label(text='матрица A')
matrix_text = tk.Text(height=6,width=50)
lblmin= tk.Label(text='минимальный эл. в заштрихованной области')
min_text = tk.Text(height=1,width=5)
lblmax= tk.Label(text='максимальный эл. в заштрихованной области')
max_text = tk.Text(height=1,width=5)
lblvect = tk.Label(text='вектор с')
vect_text = tk.Text(height=1,width=100)
lblsvect = tk.Label(text='сортированный вектор с')
svect_text = tk.Text(height=1,width=100)





btn1.pack()
lblmatrix.pack()
matrix_text.pack()
lblmin.pack()
min_text.pack()
lblmax.pack()
max_text.pack()
lblvect.pack()
vect_text.pack()
lblsvect.pack()
svect_text.pack()
tk.mainloop()