import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from servicetypesave import *
from servicetypefind import *
from servicetypedelete import *
from servicetypeload import *
from servicetypeupdate import *
from servicetypenavigate import *
from tkinter import PhotoImage
def showservicetypedashboard():
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#F2E9E4')
    t.title('service type')
    
    heading=Label(t,text='SERVICE TYPE',bg='#F2E9E4',fg='black',font=('arial',40))
    heading.place(x=550,y=5)
    bt1=Button(t,text='Save',width=30,height=5,bg='#4FA3A5',command=showservicetypesave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=5,bg='#E07A5F',command=showservicetypedelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=5,bg='#81B29A',command=showservicetypefind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=5,bg='#F2CC8F',command=showservicetypeupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=5,bg='#9D79BC',command=showservicetypeload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=5,bg='#5C7AEA',command=showservicetypenavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Documents/AQ spyder project/service_type_bg.png')
    me=Label(t,image=img,bg='#F2E9E4')
    me.place(x=400,y=70)
    t.mainloop()