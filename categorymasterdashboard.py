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
from tkinter import PhotoImage
def showcategorymasterdashboard():
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#252A43')
    t.title('service center')
    
    heading=Label(t,text='CATEGORY MASTER',bg='#262B44',fg='yellow',font=('arial',40))
    heading.place(x=500,y=5)
    bt1=Button(t,text='Save',width=30,height=4,bg='#F23A8C',command=showcategorymastersave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=4,bg='#F2995E',command=showcategorymasterdelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=4,bg='#F6A26B',command=showcategorymasterfind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=4,bg='#6FCF97',command=showcategorymasterupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=4,bg='#BB6BD9',command=showcategorymasterload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=4,bg='#E5E7EB',command=showcategorymasternavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Documents/AQ spyder project/category master.png')
    me=Label(t,image=img,bg='#262B44')
    me.place(x=300,y=70)
    
    t.mainloop()