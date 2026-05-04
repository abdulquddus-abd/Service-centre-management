import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from servicecenterdashboard import *
from categorymasterdashboard import *
from productsdashboard import *
from servicetypedashboard import *
from staffdashboard import *
from engineersdashboard import *
from customerdashboard import *
from calldatadashboard import *
from callclosedashboard import *
from callfeedbackdashboard import *
from tkinter import PhotoImage

def showprojectbuttons():
    t=tkinter.Tk()
    t.geometry('1600x900')
    t.config(bg='#e6edf5')
    t.title('My scm')
    
    heading=Label(t,text='SCM',bg='#e6edf5',fg='black',font=('arial',50))
    heading.place(x=650,y=5)
    bt1=Button(t,text='servicecenter',width=25,height=4,bg='light blue',command=showservicecenterdashboard)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='categorymaster',width=25,height=4,bg='skyblue',command=showcategorymasterdashboard)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='products',width=25,height=4,bg='burlywood',command=showproductsdashboard)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='servicetype',width=25,height=4,bg='wheat',command=showservicetypedashboard)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='staff',width=25,height=4,bg='hotpink',command=showstaffdashboard)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='engineers',width=25,height=4,bg='orange',command=showengineersdashboard)
    bt6.place(x=250,y=50)
    bt7=Button(t,text='customer',width=25,height=4,bg='white',command=showcustomerdashboard)
    bt7.place(x=250,y=150)
    bt8=Button(t,text='calldata',width=25,height=4,bg='springgreen',command=showcalldatadashboard)
    bt8.place(x=250,y=250)
    bt9=Button(t,text='callclose',width=25,height=4,bg='thistle',command=showcallclosedashboard)
    bt9.place(x=250,y=350)
    bt10=Button(t,text='callfeedback',width=25,height=4,bg='lightgrey',command=showcallfeedbackdashboard)
    bt10.place(x=250,y=450)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Pictures/Documents/__pycache__/scmm.png')
    me=Label(t,image=img,bg='#e6edf5')
    me.place(x=500,y=100)
    t.mainloop()