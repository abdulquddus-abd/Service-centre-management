import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from callclosesave import *
from callclosefind import *
from callclosedelete import *
from callcloseload import *
from callcloseupdate import *
from callclosenavigate import *
from tkinter import PhotoImage
def showcallclosedashboard():

    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#FF9AEF')
    t.title('Call close')
    
    heading=Label(t,text='CALL CLOSE',bg='#FF9AEF',fg='black',font=('arial',40))
    heading.place(x=300,y=5)
    bt1=Button(t,text='Save',width=30,height=5,bg='#E0BBE4',command=showcallclosesave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=5,bg='#FFB7C5',command=showcallclosedelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=5,bg='#D8B4FE',command=showcallclosefind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=5,bg='#FFC8DD',command=showcallcloseupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=5,bg='#F3C4FB',command=showcallcloseload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=5,bg='#F3C4FB',command=showcallclosenavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Pictures/Screenshot 2026-04-18 193051.png')
    me=Label(t,image=img,bg='#FF9AEF')
    me.place(x=400,y=100)
    t.mainloop()