import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from servicecentersave import *
from servicecenterfind import *
from servicecenterdelete import *
from servicecenterload import *
from servicecenterupdate import *
from servicecenternavigate import *


t=tkinter.Tk()
t.geometry('500x500')
t.config(bg='light pink')
t.title('service center')

heading=Label(t,text='SERVICE CENTER',bg='lightpink',fg='black',font=('arial',20))
heading.place(x=150,y=5)
bt1=Button(t,text='Save',width=15,command=showservicecentersave)
bt1.place(x=50,y=50)
bt2=Button(t,text='Delete',width=15,command=showservicecenterdelete)
bt2.place(x=50,y=90)
bt3=Button(t,text='Find',width=15,command=showservicecenterfind)
bt3.place(x=50,y=130)
bt4=Button(t,text='Update',width=15,command=showservicecenterupdate)
bt4.place(x=50,y=170)
bt5=Button(t,text='show',width=15,command=showservicecenterload)
bt5.place(x=50,y=210)
bt6=Button(t,text='Navigate',width=15,command=showservicecenternavigate)
bt6.place(x=50,y=250)

t.mainloop()