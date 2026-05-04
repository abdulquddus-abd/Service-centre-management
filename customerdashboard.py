import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from customersave import *
from customerfind import *
from customerdelete import *
from customerload import *
from customerupdate import *
from customernavigate import *
from tkinter import PhotoImage
def showcustomerdashboard():

    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='white')
    t.title('Engineers')
    
    heading=Label(t,text='CUSTOMERS',bg='white',fg='black',font=('calibri',40))
    heading.place(x=300,y=5)
    bt1=Button(t,text='Save',width=30,height=5,bg="#E9EEF5",command=showcustomersave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=5,bg="#FFF8E7",command=showcustomerdelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=5,bg="#F8F9FA",command=showcustomerfind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=5,bg="#F1F3F5",command=showcustomerupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=5,bg="#FDF6EC",command=showcustomerload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=5,bg="#EEF2F7",command=showcustomernavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Pictures/customrrs.png')
    me=Label(t,image=img,bg='white')
    me.place(x=400,y=100)
    t.mainloop()