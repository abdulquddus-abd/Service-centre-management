import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from staffsave import *
from stafffind import *
from staffdelete import *
from staffupdates import *
from staffload import *
from staffnavigate import *
from tkinter import PhotoImage
def showstaffdashboard():
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#ff5c8a')
    t.title('Staff')
    
    heading=Label(t,text='STAFF',bg='#FF5C8A',fg='black',font=('arial',40))
    heading.place(x=300,y=5)
    bt1=Button(t,text='Save',width=30,height=5,bg='#FFFFFF',command=showstaffsave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=5,bg='#222222',fg='white',command=showstaffdelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=5,bg='#008080',fg='#FFC857',command=showstafffind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=5,bg='#3EB489',command=showstaffupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=5,bg='#FFC857',command=showstaffload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=5,bg='#0a1f44',fg='white',command=showstaffnavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Pictures/Documents/stafff.png')
    me=Label(t,image=img,bg='#FF5C8A')
    me.place(x=400,y=70)
    t.mainloop()