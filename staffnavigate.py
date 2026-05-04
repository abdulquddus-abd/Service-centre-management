import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
xa=[] 
xb=[] 
xc=[] 
xd=[]  
xe=[] 
i=0 


def showstaffnavigate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('find screen')
    
    
   
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select * from staff"
        global xa,xb,xc,xd,xe
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            xa.append(r[0])
            xb.append(r[1])
            xc.append(r[2])
            xd.append(r[3])
            xe.append(r[4])
        db.close()
    def first():
        global xa,xb,xc,xd,xe,i
        i=0
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
    def next():
        global xa,xb,xc,xd,xe,i
        i=i+1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
    def previous():
        global xa,xb,xc,xd,xe,i
        i=i-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
    def last():
        global xa,xb,xc,xd,xe,i
        i=len(xa)-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
       
        
    heading=Label(t,text='Navigate staff',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=160,y=5)
    
    l1=Label(t,text='Staff id',bg='lightpink')
    l1.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=250,y=50)
    
    l2=Label(t,text='name',bg='lightpink')
    l2.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    
    l3=Label(t,text='address',bg='lightpink')
    l3.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=250,y=130)
    
    l4=Label(t,text='email',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    l5=Label(t,text='phone',bg='lightpink')
    l5.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=250,y=210)
    
    bt=Button(t,text='First',command=first)
    bt.place(x=350,y=350)
    bt3=Button(t,text='≫',command=next)
    bt3.place(x=50,y=350)
    bt1=Button(t,text='Previous',command=previous)
    bt1.place(x=150,y=350)
    bt2=Button(t,text='Last',command=last)
    bt2.place(x=250,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
