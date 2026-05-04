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
def showproductsnavigate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    t.title('find screen')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select * from products"
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
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select prodid from products"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt    
        
    heading=Label(t,text='Navigate p',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=210,y=5)
    
    l1=Label(t,text='prodid',bg='lightpink')
    l1.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=250,y=50)
    
    l2=Label(t,text='catid',bg='lightpink')
    l2.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    
    l3=Label(t,text='pname',bg='lightpink')
    l3.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=250,y=130)
    
    l4=Label(t,text='warranty years',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    l5=Label(t,text='remarks',bg='lightpink')
    l5.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=250,y=210)
    
    bt=Button(t,text='first',command=first)
    bt.place(x=350,y=300)
    bt3=Button(t,text='next',command=next)
    bt3.place(x=50,y=300)
    bt1=Button(t,text='previous',command=previous)
    bt1.place(x=150,y=300)
    bt2=Button(t,text='last',command=last)
    bt2.place(x=250,y=300)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
