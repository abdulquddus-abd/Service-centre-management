import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showservicetypedelete():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('find screen')
    
    
    def delete():
        if len(xa.get())==0:
            msg.config(text='Pls fill Serviceid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from servicetype where serviceid=%d"%(xa)
            cur.execute(sql)
            db.commit()
            db.close()
            msg.config(text="Data deleted,thanks")
            e1.delete(0,END)
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select serviceid from servicetype"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt    
        
    heading=Label(t,text='Delete st',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=200,y=5)
    l1=Label(t,text='serviceid',bg='lightpink')
    l1.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=250,y=50)
    
    l2=Label(t,text='prodid',bg='lightpink')
    l2.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    
    l3=Label(t,text='catid',bg='lightpink')
    l3.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=250,y=130)
    
    l4=Label(t,text='email',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    l5=Label(t,text='name',bg='lightpink')
    l5.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=250,y=210)
    
    l6=Label(t,text='charges',bg='lightpink')
    l6.place(x=50,y=250)
    e6=Entry(t,width=20)
    e6.place(x=250,y=250)
    
    l7=Label(t,text='durationdays',bg='lightpink')
    l7.place(x=50,y=290)
    e7=Entry(t,width=20)
    e7.place(x=250,y=290)
    
    
    
    bt=Button(t,text='Delete',command=delete)
    bt.place(x=350,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
