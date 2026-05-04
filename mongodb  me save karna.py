import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient



t=tkinter.Tk()
t.geometry('700x700')
t.config(bg='black')
def savedata():
    db=MongoClient('localhost',27017)
    data=db['mymongo1011']
    ct=data['Employee']
    xa=int(e1.get())
    xb=e2.get()
    xc=e3.get()
    xd=int(e4.get())
    dt={'empid':xa,'name':xb,'city':xc,'salary':xd}
    ct.insert_one(dt)
    messagebox.showinfo('hi','saved')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    db.close()

l1=Label(t,text='Empid',bg='black',fg='white')
l1.place(x=50,y=50)
e1=Entry(t,width=20)
e1.place(x=300,y=50)
l2=Label(t,text='Name',bg='black',fg='white')
l2.place(x=50,y=90)
e2=Entry(t,width=20)
e2.place(x=300,y=90)
l3=Label(t,text='City',bg='black',fg='white')
l3.place(x=50,y=130)
e3=Entry(t,width=20)
e3.place(x=300,y=130)
l4=Label(t,text='Salary',bg='black',fg='white')
l4.place(x=50,y=170)
e4=Entry(t,width=20)
e4.place(x=300,y=170)


bt=Button(t,text='save',command=savedata)
bt.place(x=200,y=300)


t.mainloop()
