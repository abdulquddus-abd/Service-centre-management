import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
t=tkinter.Tk()
t.geometry('500x500')
t.config(bg='lightgrey')
t.title('login screen')
def savedata():
    db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
    cur=db.cursor()
    xa=e1.get()
    xb=e2.get()
    xc=e3.get()
    sql="insert into logintable values('%s','%s','%s')"%(xa,xb,xc)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo('Hi','saved')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    
heading=Label(t,text='Login table',bg='lightgrey',fg='Black',font=('arial',20))
heading.place(x=170,y=5)
l1=Label(t,text='Login id',bg='lightgrey')
l1.place(x=50,y=50)
e1=ttk.Combobox(t)
e1.place(x=250,y=50)

l2=Label(t,text='Password',bg='lightgrey')
l2.place(x=50,y=90)
e2=Entry(t,width=20)
e2.place(x=250,y=90)

l3=Label(t,text='Email',bg='lightgrey')
l3.place(x=50,y=130)
e3=Entry(t,width=20)
e3.place(x=250,y=130)

bt=Button(t,text='Save',command=savedata)
bt.place(x=150,y=300)
bt=Button(t,text='Close')
bt.place(x=250,y=300)
t.mainloop()