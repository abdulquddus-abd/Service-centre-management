import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from categorymastersave import *
from categorymasterfind import *
from categorymasterdelete import *
from categorymasterload import *
from categorymasterupdate import *
from categorymasternavigate import *

t=tkinter.Tk()
t.geometry('500x500')
t.config(bg='light pink')
t.title('service center')

heading=Label(t,text='CATEOGORY MASTER',bg='lightpink',fg='black',font=('arial',20))
heading.place(x=150,y=5)
bt1=Button(t,text='Save',width=15,command=showcategorymastersave)
bt1.place(x=50,y=50)
bt2=Button(t,text='Delete',width=15,command=showcategorymasterdelete)
bt2.place(x=50,y=90)
bt3=Button(t,text='Find',width=15,command=showcategorymasterfind)
bt3.place(x=50,y=130)
bt4=Button(t,text='Update',width=15,command=showcategorymasterupdate)
bt4.place(x=50,y=170)
bt5=Button(t,text='show',width=15,command=showcategorymasterload)
bt5.place(x=50,y=210)
bt6=Button(t,text='Navigate',width=15,command=showcategorymasternavigate)
bt6.place(x=50,y=250)

t.mainloop()