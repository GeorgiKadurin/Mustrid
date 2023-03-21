



from tkinter import *
from tkinter import font # vajalik teksti fondi muutmiseks
from math import*
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=1000, height=800, background="white")
tahvel.grid()
9

# ühendatud kriipsud (suvaline arv koordinaatide paare)
tahvel.create_line(30,50,  300,50,  width=52 , fill="blue")
tahvel.create_line(30,100,  300,100,  width=52 , fill="black")
tahvel.create_line(30,150,  300,150,  width=52 , fill="#fafaf7")



tahvel.create_line(30,200,  300,200,  width=52 , fill="#28b5b0")
tahvel.create_line(30,250,  300,250,  width=52 , fill="#dbc81f")
tahvel.create_line(30,300,  300,300,  width=52 , fill="#28b5b0")
tahvel.create_polygon([30,174],[150,250],[30,325],fill="black")

tahvel.create_line(30,450,  300,450,  width=150 , fill="#fafaf7")
tahvel.create_oval(215, 500, 115, 400, fill="red")


k=10
x0=0
y0=0
x1=600
y1=600
a=300
r=(a**2+a**2)**(1/2)
p=(a-r)

#for i in range(12):
#    x0+=p
#    y0+=p
#    x1-=p
#    y1-=p
    
#    tahvel.create_rectangle(x0,y0,x1,y1, width=1, fill="red" )
#    tahvel.create_oval(x0, y0, x1, y1,width=1, fill="yellow")
#    p=r-a
#    r=r-p
#    a=((r)*sqrt(2))/2
#tahvel.grid()


tahvel.grid()


#x1=50
#y1=x1*8
#for i in range(8):
#    for j in range (8):
#        x2=i*x1
#        y2=j*x1
#        if(i+j)%2==0:
#            color="white"
#        else:
#            color="black"
#        x=tahvel.create_rectangle(x2,y2,x2+x1,y2+x1,fill=color)






    #tahvel.create_line(420,400,  470,400,  width=45 , fill="red")
    #tahvel.create_line(420,450,  470,450,  width=45 , fill="yellow")





tahvel.create_line(320,550,  570,550,  width=500 , fill="#a3a7ad")
suur_font = font.Font(family='Helvetica', size=20, weight='bold')
tahvel.create_text(370, 310, text="Valgusfoor", font=suur_font, anchor=NW)
tahvel.create_line(420,400,  470,400,  width=45 , fill="red")
tahvel.create_line(420,450,  470,450,  width=45 , fill="yellow")
tahvel.create_line(420,500,  470,500,  width=45 , fill="green")

tahvel.create_line(445 ,530,  445,750,  width=8 , fill="black")
tahvel.create_line(350,760,  530,760,  width=4 , fill="black")


raam.mainloop()











#from tkinter import *
#from tkinter import font # vajalik teksti fondi muutmiseks

#raam = Tk()
#raam.title("Tahvel")
#tahvel = Canvas(raam, width=600, height=600, background="white")
#tahvel.grid()



## ristkülik
#tahvel.create_rectangle(30,260,  300,300)

## ovaal
#tahvel.create_oval(30,260,  300,300, width=2, outline="blue", fill="wheat")


#raam.mainloop()


