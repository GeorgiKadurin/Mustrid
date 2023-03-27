from tkinter import *
from random import choice
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

def valik4():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=350, height=350, background="white")
    tahvel.grid()

    k=10
    x0=100
    y0=100
    x1=300
    y1=300
    a=102
    r=(a**2+a**2)**(1/2)
    p=(a-r)

    for i in range(12):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
    
        tahvel.create_rectangle(x0,y0,x1,y1, width=1, fill="red" )
        tahvel.create_oval(x0, y0, x1, y1,width=1, fill="yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2
    tahvel.grid()


def valik5():
        raam = Tk()
        raam.title("Tahvel")
        tahvel = Canvas(raam, width=350, height=350, background="white")
        tahvel.grid()

        x1=35
        y1=x1*8
        for x in range(8):
            for c in range (8):
                x2=x*x1
                y2=c*x1
                if(x+c)%2==0:
                    color="white"
                else:
                    color="black"
                y=tahvel.create_rectangle(x2,y2,x2+x1,y2+x1,fill=color)




def valik6():

        colors=["black",
            "red",
            "blue",
            "gray",
            "yellow",
            "green",
            "lightblue",
            "pink",
            "gold",
            "cyan",
            "magenta"]
        raam2=Tk()
        raam2.title("Ringid")
        tahvel2=Canvas(raam2,width=600,  height=600, background="white")
        x0=0
        y0=0
        x1=600
        y1=600
        p=5
        for i in range(55):
            x0+=p
            y0+=p
            x1-=p
            y1-=p
            tahvel2.create_oval(x0,y0,x1,y1, fill=choice(colors))
        tahvel2.grid()
        
        raam2.mainloop
 
def valik7():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=650, height=800, background="white")
    tahvel.grid()

    tahvel.create_line(320,550,  570,550,  width=500 , fill="#5c5959")
    suur_font = font.Font(family='Helvetica', size=20, weight='bold')
    tahvel.create_text(370, 310, text="Valgusfoor", font=suur_font, anchor=NW)
    tahvel.create_line(420,400,  470,400,  width=45 , fill="gray")
    tahvel.create_line(420,450,  470,450,  width=45 , fill="gray")
    tahvel.create_line(420,500,  470,500,  width=45 , fill="gray")

    tahvel.create_line(445 ,530,  445,750,  width=8 , fill="black")
    tahvel.create_line(350,760,  530,760,  width=4 , fill="black")





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
    tahvel = Canvas(raam, width=340, height=370, background="white")
    tahvel.grid()

    tahvel.create_line(30,212,  300,212,  width=52 , fill="blue")
    tahvel.create_line(30,264,  300,264,  width=52 , fill="black")
    tahvel.create_line(30,316,  300,316,  width=52 , fill="#fafaf7")

    tahvel.create_line(30,50,  300,50,  width=52 , fill="#28b5b0")
    tahvel.create_line(30,100,  300,100,  width=52 , fill="#dbc81f")
    tahvel.create_line(30,150,  300,150,  width=52 , fill="#28b5b0")
    tahvel.create_polygon([30,23],[150,100],[30,175],fill="black")


    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)

def valik_3():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=340, height=550, background="white")
    tahvel.grid()

    tahvel.create_line(30,212,  300,212,  width=52 , fill="blue")
    tahvel.create_line(30,264,  300,264,  width=52 , fill="black")
    tahvel.create_line(30,316,  300,316,  width=52 , fill="#e6e1e1")


    tahvel.create_line(30,50,  300,50,  width=52 , fill="#28b5b0")
    tahvel.create_line(30,100,  300,100,  width=52 , fill="#dbc81f")
    tahvel.create_line(30,150,  300,150,  width=52 , fill="#28b5b0")
    tahvel.create_polygon([30,23],[150,100],[30,175],fill="black")



    tahvel.create_line(30,450,  300,450,  width=150 , fill="#e6e1e1")
    tahvel.create_oval(200, 420, 130, 490, fill="red")




    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)



def valik_4():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=340, height=550, background="white")
    tahvel.grid()

    k=10
    x0=100
    y0=100
    x1=300
    y1=300
    a=102
    r=(a**2+a**2)**(1/2)
    p=(a-r)

    for i in range(12):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
    
        tahvel.create_rectangle(x0,y0,x1,y1, width=1, fill="red" )
        tahvel.create_oval(x0, y0, x1, y1,width=1, fill="yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2
    tahvel.grid()


    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)





def valik_5():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=720, height=400, background="white")
    tahvel.grid()

    k=10
    x0=400
    y0=50
    x1=630
    y1=280
    a=115
    r=(a**2+a**2)**(1/2)
    p=(a-r)

    for i in range(12):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
    
        tahvel.create_rectangle(x0,y0,x1,y1, width=1, fill="red" )
        tahvel.create_oval(x0, y0, x1, y1,width=1, fill="yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2
    tahvel.grid()


    x1=40
    y1=x1*8
    for x in range(8):
        for c in range (8):
                x2=x*x1
                y2=c*x1
                if(x+c)%2==0:
                    color="white"
                else:
                    color="black"
                y=tahvel.create_rectangle(x2,y2,x2+x1,y2+x1,fill=color)



    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)




def valik_6():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=1300, height=700, background="white")
    tahvel.grid()

    k=10
    x0=400
    y0=50
    x1=630
    y1=280
    a=115
    r=(a**2+a**2)**(1/2)
    p=(a-r)

    for i in range(12):
        x0+=p
        y0+=p
        x1-=p
        y1-=p
    
        tahvel.create_rectangle(x0,y0,x1,y1, width=1, fill="red" )
        tahvel.create_oval(x0, y0, x1, y1,width=1, fill="yellow")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2
    tahvel.grid()


    x1=40
    y1=x1*8
    for x in range(8):
        for c in range (8):
                x2=x*x1
                y2=c*x1
                if(x+c)%2==0:
                    color="white"
                else:
                    color="black"
                y=tahvel.create_rectangle(x2,y2,x2+x1,y2+x1,fill=color)


                
    colors=["black",
            "red",
            "blue",
            "gray",
            "yellow",
            "green",
            "lightblue",
            "pink",
            "gold",
            "cyan",
            "magenta"]
    x0=690
    y0=0
    x1=1300
    y1=600
    p=5
    for i in range(55):
            x0+=p
            y0+=p
            x1-=p
            y1-=p
            tahvel.create_oval(x0,y0,x1,y1, fill=choice(colors))
    tahvel.grid()
        



    val1=var1.get()
    val2=var2.get()
    val3=var3.get()
    if val1!="-":lbox.insert(END, val1)                #lbox.insert(END, val1)             
    if val2!="-":lbox.insert(END, val2)                #lbox.insert(END, val2)
    if val3!="-":lbox.insert(END, val3)

def valik_7():
    raam = Tk()
    raam.title("Tahvel")
    tahvel = Canvas(raam, width=650, height=800, background="white")
    tahvel.grid()

    tahvel.create_line(320,550,  570,550,  width=500 , fill="#5c5959")
    suur_font = font.Font(family='Helvetica', size=20, weight='bold')
    tahvel.create_text(370, 310, text="Valgusfoor", font=suur_font, anchor=NW)
    tahvel.create_line(420,400,  470,400,  width=45 , fill="red")
    tahvel.create_line(420,450,  470,450,  width=45 , fill="yellow")
    tahvel.create_line(420,500,  470,500,  width=45 , fill="green")

    tahvel.create_line(445 ,530,  445,750,  width=8 , fill="black")
    tahvel.create_line(350,760,  530,760,  width=4 , fill="black")


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
r1=Radiobutton(aken,text="Eesti lipp",variable=var, value=1, command=valik1)
r2=Radiobutton(aken,text="lipp",variable=var, value=2, command=valik2)
r3=Radiobutton(aken,text="Jaapani lipp",variable=var, value=3, command=valik3)

r4=Radiobutton(aken,text="Muster 1",variable=var, value=4, command=valik4)
r5=Radiobutton(aken,text="Muster 2",variable=var, value=5, command=valik5)
r6=Radiobutton(aken,text="Muster 3",variable=var, value=6, command=valik6)

r7=Radiobutton(aken,text="Valgusfoor off",variable=var, value=7, command=valik7)

lbox=Listbox(aken, height=3,width=30)

var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
var5=StringVar()
var6=StringVar()
var7=StringVar()

c1=Checkbutton(aken,text="Üks lipp",variable=var1, onvalue="",offvalue="-", command=valik_1)
c2=Checkbutton(aken,text="Kaks lippu",variable=var2, onvalue="",offvalue="-", command=valik_2)
c3=Checkbutton(aken,text="Kolm lippu",variable=var3, onvalue="",offvalue="-", command=valik_3)

c4=Checkbutton(aken,text="Üks M ",variable=var4, onvalue="",offvalue="-", command=valik_4)
c5=Checkbutton(aken,text="Kaks M ",variable=var5, onvalue="",offvalue="-", command=valik_5)
c6=Checkbutton(aken,text="Kolm M ",variable=var6, onvalue="",offvalue="-", command=valik_6)

c7=Checkbutton(aken,text="Valgusfoor on",variable=var7, onvalue="",offvalue="-", command=valik_7)

c1.deselect()
c2.deselect()
c3.deselect()
c4.deselect()
c5.deselect()
c6.deselect()
c7.deselect()

lbox.grid(row=0,column=0,columnspan=2)
r1.grid(row=1,column=0)
r2.grid(row=2,column=0)
r3.grid(row=3,column=0)
r4.grid(row=4,column=0)
r5.grid(row=5,column=0)
r6.grid(row=6,column=0)
r7.grid(row=7,column=0)

c1.grid(row=1,column=1)
c2.grid(row=2,column=1)
c3.grid(row=3,column=1)
c4.grid(row=4,column=1)
c5.grid(row=5,column=1)
c6.grid(row=6,column=1)
c7.grid(row=7,column=1)

aken.mainloop()



