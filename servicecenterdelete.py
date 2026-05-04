import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showservicecenterdelete():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    t.title('delete screen')
    
    def delete():
        if len(e1.get())==0:
            msg.config(text='Pls Fill Centerid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=int(e1.get())
            sql="delete from servicecenter where centerid=%d"%(xa)
            cur.execute(sql)
            db.commit()
            db.close()
            msg.config(text='Data Deleted')
            e1.delete(0,END)
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
        
    
    heading=Label(t,text='Delete sc',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=190,y=5)
    l1=Label(t,text='centerid',bg='lightpink')
    l2=Label(t,text='name',bg='lightpink')
    l3=Label(t,text='address',bg='lightpink')
    l4=Label(t,text='email',bg='lightpink')
    l5=Label(t,text='phone',bg='lightpink')
    l6=Label(t,text='regno',bg='lightpink')
    
    l1.place(x=50,y=50)
    l2.place(x=50,y=90)
    l3.place(x=50,y=130)
    l4.place(x=50,y=170)
    l5.place(x=50,y=210)
    l6.place(x=50,y=250)
    
    e1=ttk.Combobox(t)
    e2=Entry(t,width=20)
    e3=Entry(t,width=20)
    e4=Entry(t,width=20)
    e5=Entry(t,width=20)
    e6=Entry(t,width=20)
    
    e1.place(x=250,y=50)
    e2.place(x=250,y=90)
    e3.place(x=250,y=130)
    e4.place(x=250,y=170)
    e5.place(x=250,y=210)
    e6.place(x=250,y=250)
    
    bt2=Button(t,text='delete',command=delete)
    bt2.place(x=250,y=300)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
    
