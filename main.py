import tkinter as tk
from tkinter import *
import sqlite3
 
class Asos:
    def __init__(self) -> None:
        self.root1=Tk()
        
        self.root1.title("Kirish")
        self.root1.geometry("220x160")

        labelcha1=Label(self.root1,text="  ")
        labelcha2=Label(self.root1,text="  ")
        Label_top=Label(self.root1,text="Savdoni boshqaruv dasturi",font=20)
        savdo=Button(self.root1,text="Savdo bo'limi",command=self.sotish, font=20)
        qarz=Button(self.root1,text="Qarzlar bo'limi",command=self.qarzlar,font=20)
        # T = Text(root, height = 10, width = 59)
        
        # T.grid(row=1,column=1,columnspan=5)
        Label_top.grid(row=0,column=3)
        labelcha1.grid(row=1,column=0)
        savdo.grid(row=2,column=1,columnspan=3)
        labelcha2.grid(row=3,column=0)
        qarz.grid(row=4,column=1, columnspan=3)

        self.root1.mainloop()

    def sotish(self):
        self.root1.destroy()
        self.rootsavdo=Tk()
        self.rootsavdo.title("Savdo")
        self.rootsavdo.geometry("460x360")
    
        Label_top=Label(self.rootsavdo,text="Savdoni boshqaruv dasturi",font=20)
        l_massa=Label(self.rootsavdo,text="Massa",font=20,pady=10)
        self.e_massa=Entry(self.rootsavdo)
        l_narx=Label(self.rootsavdo,text="Narxi",font=20,pady=10)
        self.e_narx=Entry(self.rootsavdo)
        l_holat=Label(self.rootsavdo,text="To'lov yoki nasiya",font=20,pady=10)
        self.variable = StringVar(self.rootsavdo)
        self.e_holat=OptionMenu(self.rootsavdo, self.variable, "tulov", "qarz",command=self.tanlov)
        saqlash=Button(self.rootsavdo,text="Saqlash",command=self.saqla,font=20)
        orqaga=Button(self.rootsavdo,text="Asosiy oynaga",command=self.ortga,font=20)
        l_nimadir=Label(self.rootsavdo,text="",font=20)

        Label_top.grid(row=0,column=1)
        l_massa.grid(row=1,column=0)
        self.e_massa.grid(row=1,column=1)
        l_narx.grid(row=2,column=0)
        self.e_narx.grid(row=2,column=1)
        l_holat.grid(row=3,column=0)
        self.e_holat.grid(row=3,column=1,columnspan=2)
        saqlash.grid(row=8,column=1,columnspan=2)
        orqaga.grid(row=8,column=0)


        self.rootsavdo.mainloop()

    def saqla(self):
        if self.e_massa.get()=="" or self.e_narx.get()=="" or self.variable.get()=="":
            tasdiq=Label(self.rootsavdo,text="Ma'lumotlar to'liq to'ldirilmadi",padx=20,fg='red')
        elif self.variable=="tulov":
            conn=sqlite3.connect("data.db")
            conn.execute(f"""INSERT INTO  xarajatlar (hajmi,narxi,xolat) VALUES ({float(self.e_massa.get())},{int(self.e_narx.get())},'{self.variable.get()}')""")
            conn.commit()
            tasdiq=Label(self.rootsavdo,text="Saqlandi",padx=20,fg='green')
        elif self.variable=="qarz" and self.e_ism!="" and self.e_tel!="" and self.e_summa!="":
            conn=sqlite3.connect("data.db")
            conn.execute(f"""INSERT INTO  xarajatlar (hajmi,narxi,xolat) VALUES ({float(self.e_massa.get())},{int(self.e_narx.get())},'{self.variable.get()}')""")
            conn.execute(f"""INSERT INTO  qarzlar (ism,tel,summa,muddat) VALUES ('{self.e_ism.get()}','{self.e_tel.get()}','{self.e_summa.get()}',{int(self.e_muddat.get())})""")
            conn.commit()
            tasdiq=Label(self.rootsavdo,text="Saqlandi",padx=20,fg='green')
        else:
            tasdiq=Label(self.rootsavdo,text="Ma'lumotlar to'liq to'ldirilmadi",padx=20,fg='red')
        tasdiq.grid(row=9,column=1)
        self.rootsavdo.after(1500,tasdiq.destroy)

    def ortga(self):
        self.rootsavdo.destroy()
        self.__init__()

    def tanlov(self):
        if self.variable=="qarz":
            l_ism=Label(self.rootsavdo,text="Ism",font=20,pady=10)
            self.e_ism=Entry(self.rootsavdo)
            l_tel=Label(self.rootsavdo,text="Telefon",font=20,pady=10)
            self.e_tel=Entry(self.rootsavdo)
            l_summa=Label(self.rootsavdo,text="Summa",font=20,pady=10)
            self.e_summa=Entry(self.rootsavdo)
            l_muddat=Label(self.rootsavdo,text="Muddat (kun)",font=20,pady=10)
            self.e_muddat=Entry(self.rootsavdo)

            l_ism.grid(row=4,column=0)
            self.e_ism.grid(row=4,column=1)
            l_tel.grid(row=5,column=0)
            self.e_tel.grid(row=5,column=1)
            l_summa.grid(row=6,column=0)
            self.e_summa.grid(row=6,column=1)
            l_muddat.grid(row=6,column=0)
            self.e_muddat.grid(row=6,column=1)
        elif self.variable=="tulov":
            l_ism=Label(self.rootsavdo,text="Ism",font=20,pady=10)
            self.e_ism=Entry(self.rootsavdo)
            l_tel=Label(self.rootsavdo,text="Telefon",font=20,pady=10)
            self.e_tel=Entry(self.rootsavdo)
            l_summa=Label(self.rootsavdo,text="Summa",font=20,pady=10)
            self.e_summa=Entry(self.rootsavdo)
            l_muddat=Label(self.rootsavdo,text="Muddat",font=20,pady=10)
            self.e_muddat=Entry(self.rootsavdo)

            l_ism.destroy()
            self.e_ism.destroy()
            l_tel.destroy()
            self.e_tel.destroy()
            l_summa.destroy()
            self.e_summa.destroy()
            l_muddat.destroy()
            self.e_muddat.destroy()


    def qarzlar(self):
        self.root1.destroy()
        self.rootqarz=Tk()
        self.rootqarz.title("Savdo")
        self.rootqarz.geometry("460x360")





Asos()