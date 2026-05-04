import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from productssave import *
from productsfind import *
from productsdelete import *
from productsload import *
from productsupdate import *
from productsnavigate import *

def showproductsdashboard():
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#E8D4C6')
    t.title('service center')
    
    heading=Label(t,text='PRODUCTS',bg='#E8D4C6',fg='black',font=('arial',40))
    heading.place(x=550,y=5)
    bt1=Button(t,text='Save',width=30,height=4,bg='#2E2E2E',fg='white',command=showproductssave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=4,bg='#6E6E6E',fg='gold',command=showproductsdelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=4,bg='#C9C9C9',command=showproductsfind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=4,bg='#000000',fg='white',command=showproductsupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=4,bg='#4A90E2',command=showproductsload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=4,bg='#F5A623',command=showproductsnavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Documents/AQ spyder project/products.png')
    me=Label(t,image=img,bg='#E8D4C6')
    me.place(x=300,y=70)
    t.mainloop()