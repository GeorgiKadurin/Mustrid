
































#from tkinter import *
#from tkinter import font # vajalik teksti fondi muutmiseks

#raam = Tk()
#raam.title("Tahvel")
#tahvel = Canvas(raam, width=1240, height=940, background="white")
#tahvel.grid()


## ühendatud kriipsud (suvaline arv koordinaatide paare)
#tahvel.create_line(30,50,  300,50,  width=52 , fill="blue")
#tahvel.create_line(30,100,  300,100,  width=52 , fill="black")
#tahvel.create_line(30,150,  300,150,  width=52 , fill="#fafaf7")



#tahvel.create_line(30,200,  300,200,  width=52 , fill="#28b5b0")
#tahvel.create_line(30,250,  300,250,  width=52 , fill="#dbc81f")
#tahvel.create_line(30,300,  300,300,  width=52 , fill="#28b5b0")
#tahvel.create_polygon([30,174],[150,250],[30,325],fill="black")

#tahvel.create_line(30,450,  300,450,  width=150 , fill="#fafaf7")
#tahvel.create_oval(215, 500, 115, 400, fill="red")



#tahvel.create_rectangle(30,750,200,600, fill="red" )
#tahvel.create_oval(32, 750, 200, 600, fill="yellow")



#raam.mainloop()











##from tkinter import *
##from tkinter import font # vajalik teksti fondi muutmiseks

##raam = Tk()
##raam.title("Tahvel")
##tahvel = Canvas(raam, width=600, height=600, background="white")
##tahvel.grid()

### üksik kriips (x0, y0, x1, y1)
##tahvel.create_line(30, 40, 300, 40)

### ühendatud kriipsud (suvaline arv koordinaatide paare)
##tahvel.create_line(30,60,  300,60,  300,100,  60,100)

### võimalik on muuta joone paksust (width) ja sisu värvi (fill)
##tahvel.create_line(30, 130, 300, 130, width=4, fill="red")

### teistsugune joone stiil
##tahvel.create_line(30, 150, 300, 150, width=5, dash=(5, 1, 2, 1), arrow=LAST)

### tõmbab kriipsud, ühendab otsapunktid ja värvib sisu
### värve saab määrata ka rgb komponentidena
### vt. http://www.colorpicker.com/
##tahvel.create_polygon(30,160,  300,160,  300,200,  60,200, fill="#95BD9D")

### ristkülik
##tahvel.create_rectangle(30,260,  300,300)

### ovaal
##tahvel.create_oval(30,260,  300,300, width=2, outline="blue", fill="wheat")

### proovi liigutada hiirt selle ovaali kohale
##tahvel.create_oval(330, 330, 400, 400, fill="gray", activefill="pink")

### kui soovid teksti esitamisel ise fonti valida, siis tuleb enne vastav font luua
##suur_font = font.Font(family='Helvetica', size=32, weight='bold')
##tahvel.create_text(30, 500, text="Tere!", font=suur_font, anchor=NW)

##raam.mainloop()



