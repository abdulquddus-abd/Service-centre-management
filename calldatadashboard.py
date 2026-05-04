import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from calldatasave import *
from calldatafind import *
from calldatadelete import *
from calldataload import *
from calldataupdate import *
from calldatanavigate import *
from tkinter import PhotoImage
def showcalldatadashboard():
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#F7F9FB')
    t.title('Engineers')
    
    heading=Label(t,text='CALL DATA',bg='white',fg='black',font=('arial',40))
    heading.place(x=300,y=5)
    bt1=Button(t,text='Save',width=30,height=4,bg='#1FC8B3',command=showcalldatasave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=4,bg='#FF7A6A',command=showcalldatadelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=4,bg='#FF8A5C',command=showcalldatafind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=4,bg='#5B4BDB',command=showcalldataupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=4,bg='#A3D94E',command=showcalldataload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=4,bg='#4CD4B0',command=showcalldatanavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Pictures/Documents/caaaal.png')
    me=Label(t,image=img)
    me.place(x=400,y=100)
    t.mainloop()