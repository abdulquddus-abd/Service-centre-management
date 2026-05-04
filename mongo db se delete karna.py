import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient


t=tkinter.Tk()
t.geometry('700x700')
t.config(bg='hotpink')
def deletedata():
    db=MongoClient('localhost',27017)
    data=db['mymongo1011']
    ct=data['Employee']
    xa=int(e1.get())
    ct.delete_one({'empid':xa})
    messagebox.showinfo('hi','Deleted')
    e1.delete(0,END)
    db.close()

l1=Label(t,text='Empid',bg='hotpink',fg='black')
l1.place(x=50,y=50)
e1=Entry(t,width=20)
e1.place(x=300,y=50)
l2=Label(t,text='Name',bg='hotpink',fg='black')
l2.place(x=50,y=90)
e2=Entry(t,width=20)
e2.place(x=300,y=90)
l3=Label(t,text='City',bg='hotpink',fg='black')
l3.place(x=50,y=130)
e3=Entry(t,width=20)
e3.place(x=300,y=130)
l4=Label(t,text='Salary',bg='hotpink',fg='black')
l4.place(x=50,y=170)
e4=Entry(t,width=20)
e4.place(x=300,y=170)


bt=Button(t,text='DELETE',command=deletedata)
bt.place(x=200,y=300)


t.mainloop()
