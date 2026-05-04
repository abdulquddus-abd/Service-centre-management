import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from engineerssave import *
from engineersfind import *
from engineersdelete import *
from engineersload import *
from engineersupdate import *
from engineersnavigate import *#navigatexxx
from tkinter import PhotoImage
def showengineersdashboard():
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#F7931A')
    t.title('Engineers')
    
    heading=Label(t,text='ENGINEERS',bg='#F7931A',fg='black',font=('calibri',40))
    heading.place(x=300,y=5)
    bt1=Button(t,text='Save',width=30,height=5,bg='#BAE6FD',command=showengineerssave)
    bt1.place(x=50,y=50)
    
    bt2=Button(t,text='Delete',width=30,height=5,bg='#CFFAFE',command=showengineersdelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=5,bg='#D1FAE5',command=showengineersfind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=5,bg='#CCFBF1',command=showengineersupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=5,bg='#EDE9FE',command=showengineersload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=5,bg="lightyellow",command=showengineersnavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Pictures/Documents/enggggg.png')
    me=Label(t,image=img,bg='#F7931A')
    me.place(x=400,y=70)
    t.mainloop()