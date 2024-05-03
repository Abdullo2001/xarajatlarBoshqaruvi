import tkinter as tk
from tkinter import *
import sqlite3

root=Tk()

#Savdo-------------------------------------------------------------------------------------

def sotish(root):
    
    rootsavdo=Tk()

    rootsavdo.mainloop()

#Funksiyalar---------------------------------------------------------------------------------------

def qarzlar():
    pass
#Kirish-----------------------------------------------------------------------------------
root.title("Kirish")
root.geometry("220x160")

labelcha1=Label(root,text="  ")
labelcha2=Label(root,text="  ")
Label_top=Label(root,text="Savdoni boshqaruv dasturi",font=20)
savdo=Button(root,text="Savdo bo'limi",command=lambda: sotish(root), font=20)
qarz=Button(root,text="Qarzlar bo'limi",command=qarzlar,font=20)
# T = Text(root, height = 10, width = 59)

# T.grid(row=1,column=1,columnspan=5)
Label_top.grid(row=0,column=3)
labelcha1.grid(row=1,column=0)
savdo.grid(row=2,column=1,columnspan=3)
labelcha2.grid(row=3,column=0)
qarz.grid(row=4,column=1, columnspan=3)

root.mainloop()



