import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from servicecentersave import *
from servicecenterfind import *
from servicecenterdelete import *                                   
from servicecenterload import *
from tkinter import PhotoImage
from servicecenterupdate import *
from servicecenternavigate import *


def showservicecenterdashboard():
    
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#29BFC2')
    t.title('service center')
    
    heading=Label(t,text='SERVICE CENTER',bg='#29BFC2',fg='black',font=('arial',40))
    heading.place(x=300,y=5)
    bt1=Button(t,text='Save',width=30,height=4,bg='#E53935',command=showservicecentersave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=4,bg='#FBC02D',command=showservicecenterdelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=4,bg='#43A047',command=showservicecenterfind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=4,bg='#81D4FA',command=showservicecenterupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=4,bg='#BDBDBD',command=showservicecenterload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=4,command=showservicecenternavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Documents/AQ spyder project/servicecentere.png')
    me=Label(t,image=img,bg='#29BFC2')
    me.place(x=400,y=70)
    t.mainloop()