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
def showcategorymasternavigate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    t.title('navigate screen')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        sql="select * from categorymaster"
        global xa,xb,xc
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            xa.append(r[0])
            xb.append(r[1])
            xc.append(r[2])
        db.close()
    def first():
        global xa,xb,xc,i
        i=0
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    def next():
        global xa,xb,xc,i
        i=i+1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    def previous():
        global xa,xb,xc,i
        i=i-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    def last():
        global xa,xb,xc,i
        i=len(xa)-1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    
    
    heading=Label(t,text='Navigate cm',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=160,y=5)
    l1=Label(t,text='catid',bg='lightpink')
    l2=Label(t,text='catname',bg='lightpink')
    l3=Label(t,text='remarks',bg='lightpink')
    l1.place(x=50,y=50)
    l2.place(x=50,y=90)
    l3.place(x=50,y=130)
    
    e1=Entry(t,width=20)
    e2=Entry(t,width=20)
    e3=Entry(t,width=20)
    
    e1.place(x=250,y=50)
    e2.place(x=250,y=90)
    e3.place(x=250,y=130)
    
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
    
    
