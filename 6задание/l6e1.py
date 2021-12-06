# -- coding: utf-8 --
from tkinter import *
from tkinter import ttk


window = Tk() 
def zad1():
    y = ''
    N = int(txte1.get())
    x = 0
    i = 1
    while x <= N:
        x = i**2
        i += 1
        if x <= N:
            y = y + str(x) + " "
    lble1.config(text="Ответ: "+y)
def zad2():
    a = int(txte2.get())
    n = 2
    if a >= 2:
        while a % n != 0:
            n += 1
        lble2.config(text="Ответ: "+str(n))
    else:
        lble2.config(text="Ответ: Число меньше 2")
def zad3():
    N = int(txte3.get())
    a = 1
    while 2 ** a < N:
       a += 1
    else:
        lble32.config(text='Показатель степени:'+str(a -1))
        lble31.config(text='Степень:'+str(2 ** (a - 1)))
def zad4():
    x = float(txte4.get())
    y = float(txte41.get())
    n = 0 #количество дней
    while x < y:
        n += 1
        x = x + x * 0.1
    else:
        lble42.config(text="Ответ:"+str(n))
i = 0
def zad5():
    global i
    txte5.focus()
    n = int(txte5.get())
    if n != 0:
        i += 1
        print (i)
        lble51.config(text="Введено чисел:" +str(i))   
    else:
        lble51.config(text="Количество чисел:" +str(i))
        i = 0
    txte5.delete(0, END)
n = 0
s = 0
def zad6():
    global n
    a = int(txte6.get())
    global s
    if a != 0:
        n += 1
        s += a
        a = int(txte6.get())
    lble61.config(text="Ср. знач. чисел:" +str(s/n))

def zad7():
    global n
    a = int(txte7.get())
    global s
    if a != 0:
        if a > s:
            n += 1
        s = a
        a = int(txte7.get())
    lble71.config(text="Элементов больше предыдущего:" +str(n - 1))

b = 0
m = 0
def zad8():
    a = int(txte8.get())
    global b
    global n
    global m
    if a != 0:
        if b == a:
            n += 1
        else:
            b = a
            m = max(m, n)
            n = 1
        a = int(txte8.get())
    m = max(m, n)
    lble81.config(text="Повт. элементов" +str(m))
  
 
window.title("Задание 6")  
window.geometry('500x200')  
tab_control = ttk.Notebook(window)
#1 задание
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Задание 1')
lble1 = Label(tab1,  text="Введите число:")
lble1.grid(column=0, row=1)
txte1 = Entry(tab1, width=5)
txte1.grid(column=1, row=1) 
btn = Button(tab1, text="²", command= zad1)
btn.grid(column=2, row=1) 
lble1 = Label(tab1, text="Ответ")
lble1.grid(column=4, row=2)  
#2 задание
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Задание 2')
lble2 = Label(tab2, text="Введите число:")
lble2.grid(column=0, row=1)
txte2 = Entry(tab2,width=5)
txte2.grid(column=1, row=1)
btn = Button(tab2, text="Найти наменьший натур. дел.", command= zad2)
btn.grid(column=2, row=1) 
lble2 = Label(tab2, text="Ответ")
lble2.grid(column=4, row=2)
#3 задание
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Задание 3')
lble3 = Label(tab3, text="Введите число:")
lble3.grid(column=0, row=1)
lble31 = Label(tab3, text="")
lble31.grid(column=0, row=4)
txte3 = Entry(tab3,width=5)
txte3.grid(column=1, row=1) 
btn = Button(tab3, text="Найти наибольшую целую степень двойки, не превосходящую N", command= zad3)
btn.grid(column=2, row=1) 
lble32 = Label(tab3, text="Ответ")
lble32.grid(column=0, row=3)
#4 задание
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='Задание 4')
lble4 = Label(tab4, text="Введите количесnво километров в первый день:")
lble4.grid(column=0, row=1)
lble41 = Label(tab4, text="Введите нужное количество километров:")
lble41.grid(column=0, row=2)
txte4 = Entry(tab4,width=5)
txte4.grid(column=1, row=1) 
txte41 = Entry(tab4,width=5)
txte41.grid(column=1, row=2)
btn = Button(tab4, text="Найти", command= zad4)
btn.grid(column=2, row=2) 
lble42 = Label(tab4, text="Ответ")
lble42.grid(column=0, row=3)
#5 задание
tab5 = ttk.Frame(tab_control)
tab_control.add(tab5, text='Задание 5')
lble5 = Label(tab5, text="Введите последовательность оканчивающуюся 0")
lble5.grid(column=0, row=0)
txte5 = Entry(tab5,width=5)
txte5.grid(column=1, row=0)
lble51 = Label(tab5, text="Количество чисел:")
lble51.grid(column=0, row=2)
btn = Button(tab5, text="Найти", command= zad5)
btn.grid(column=2, row=0) 
#6 задание
tab6 = ttk.Frame(tab_control)
tab_control.add(tab6, text='Задание 6')
lble6 = Label(tab6, text="Введите последовательность оканчивающуюся 0")
lble6.grid(column=0, row=0)
txte6 = Entry(tab6,width=5)
txte6.grid(column=1, row=0)
lble61 = Label(tab6, text="Ср. знач. чисел:")
lble61.grid(column=0, row=2)
btn = Button(tab6, text="Найти", command= zad6)
btn.grid(column=2, row=0) 
#7 задание
tab7 = ttk.Frame(tab_control)
tab_control.add(tab7, text='Задание 7')
lble7 = Label(tab7, text="Введите последовательность оканчивающуюся 0")
lble7.grid(column=0, row=0)
txte7 = Entry(tab7,width=5)
txte7.grid(column=1, row=0)
lble71 = Label(tab7, text="Элементов больше предыдущего:")
lble71.grid(column=0, row=2)
btn = Button(tab7, text="Найти", command= zad7)
btn.grid(column=2, row=0) 
#8 задание
tab8 = ttk.Frame(tab_control)
tab_control.add(tab8, text='Задание 8')
lble8 = Label(tab8, text="Введите последовательность оканчивающуюся 0")
lble8.grid(column=0, row=0)
txte8 = Entry(tab8,width=5)
txte8.grid(column=1, row=0)
lble81 = Label(tab8, text="Повт. элементов:")
lble81.grid(column=0, row=2)
btn = Button(tab8, text="Найти", command= zad7)
btn.grid(column=2, row=0) 
##
tab_control.pack(expand=1, fill='both')
window.mainloop()