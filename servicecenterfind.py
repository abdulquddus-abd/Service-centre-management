import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showservicecenterfind():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('find screen')
    
    def finddata():
        if len(e1.get())==0:
            msg.config(text='Pls Fill Centerid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select centerid,name,address,email,phone,regno from servicecenter where centerid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
           
            e2.insert(0,data[0])
            e3.insert(0,data[1])
            e4.insert(0,data[2])
            e5.insert(0,data[3])
            e6.insert(0,data[4])
            
            db.close()
            msg.config(text='Data founded')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select centerid from servicecenter"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt    
        
    heading=Label(t,text='Find sc',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=200,y=5)
    l1=Label(t,text='centerid',bg='lightpink')
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
    
    l6=Label(t,text='regno',bg='lightpink')
    l6.place(x=50,y=250)
    e6=Entry(t,width=20)
    e6.place(x=250,y=250)
    
    
    
    bt=Button(t,text='find',command=finddata)
    bt.place(x=350,y=300)
    
    filldata()
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    t.mainloop()
