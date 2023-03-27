from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
from math import*


def valik1():
    
        raam = Tk()
        raam.title("Tahvel")
        tahvel = Canvas(raam, width=350, height=200, background="white")
        tahvel.grid()

        tahvel.create_line(30,50,  300,50,  width=52 , fill="blue")
        tahvel.create_line(30,100,  300,100,  width=52 , fill="black")
        tahvel.create_line(30,150,  300,150,  width=52 , fill="#fafaf7")

def valik2():
        raam = Tk()
        raam.title("Tahvel")
        tahvel = Canvas(raam, width=350, height=200, background="white")
        tahvel.grid()

        tahvel.create_line(30,50,  300,50,  width=52 , fill="#28b5b0")
        tahvel.create_line(30,100,  300,100,  width=52 , fill="#dbc81f")
        tahvel.create_line(30,150,  300,150,  width=52 , fill="#28b5b0")
        tahvel.create_polygon([30,23],[150,100],[30,175],fill="black")

def valik3():
        raam = Tk()
        raam.title("Tahvel")
        tahvel = Canvas(raam, width=350, height=200, background="white")
        tahvel.grid()

        tahvel.create_line(30,90,  300,90,  width=150 , fill="#fafaf7")
        tahvel.create_oval(220, 50, 140, 120, fill="red")



def valik_1():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=350, height=200, background="white")
    tahvel.grid()

    tahvel.create_line(30,50,  300,50,  width=52 , fill="blue")
    tahvel.create_line(30,100,  300,100,  width=52 , fill="black")
    tahvel.create_line(30,150,  300,150,  width=52 , fill="#fafaf7")

    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)


def valik_2():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=350, height=200, background="white")
    tahvel.grid()


    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)

def valik_3():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=350, height=200, background="white")
    tahvel.grid()


    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)

aken=Tk()
aken.title("Erinevad nupud")
aken.geometry("200x300")

var=IntVar() #StringVar()
r1=Radiobutton(aken,text="Esimene",variable=var, value=1, command=valik1)
r2=Radiobutton(aken,text="Teine",variable=var, value=2, command=valik2)
r3=Radiobutton(aken,text="Kolmas",variable=var, value=3, command=valik3)
lbox=Listbox(aken, height=3,width=30)

var1=StringVar()
var2=StringVar()
var3=StringVar()

c1=Checkbutton(aken,text="Esimine",variable=var1, onvalue="Esimene",offvalue="-",command=valik_1)
c2=Checkbutton(aken,text="Teine",variable=var2, onvalue="Teine",offvalue="-",command=valik_2)
c3=Checkbutton(aken,text="Kolmas",variable=var3, onvalue="Kolmas",offvalue="-",command=valik_2)

c1.deselect()
c2.deselect()
c3.deselect()





lbox.grid(row=0,column=0,columnspan=2)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)

c1.grid(row=1,column=1)
c2.grid(row=2,column=1)
c3.grid(row=3,column=1)

aken.mainloop()












import tkinter as tk

def show_flag():
    # Создание окна
    window = tk.Toplevel()
    window.title("Флаг")
    
    # Создание холста
    canvas = tk.Canvas(window, width=200, height=150)
    canvas.pack()
    
    # Нарисовать флаг
    canvas.create_rectangle(0, 0, 200, 50, fill="red")
    canvas.create_rectangle(0, 50, 200, 100, fill="white")
    canvas.create_rectangle(0, 100, 200, 150, fill="blue")
    canvas.create_oval(75, 25, 125, 75, fill="white")
    
# Создание окна
root = tk.Tk()
root.title("Мой GUI")

# Создание кнопки
button = tk.Button(root, text="Показать флаг", command=show_flag)
button.pack()

# Запуск главного цикла окна
root.mainloop()
