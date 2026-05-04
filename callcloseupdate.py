import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from tkcalendar import DateEntry
def showcallcloseupdate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('Update screen')
    def finddata():
        if len(e1.get())==0:
            msg.config(text='Pls Fill Serviceid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select callno,custid,engid,dateofclose from callclose where callno='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
           
            e2.insert(0,data[1])
            e3.insert(0,data[2])
            e4.insert(0,data[3])
          
            db.close()
            msg.config(text='Data founded')
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
    
        sql="update callclose set custid='%s',engid='%s',dateofclose='%s' where callno='%s'"%(xb,xc,xd,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        msg.config(text='Data Updated,Thanks')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select callno from callclose"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt
        
    heading=Label(t,text='Callclose update',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=170,y=5)
    l1=Label(t,text='Call no',bg='lightpink')
    l1.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=250,y=50)
    
    l2=Label(t,text='Custid',bg='lightpink')
    l2.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    
    l3=Label(t,text='Eng id',bg='lightpink')
    l3.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=250,y=130)
    
    l4=Label(t,text='Date of close',bg='lightpink')
    l4.place(x=50,y=170)
    e4=DateEntry(t,width=20,bg='lightgreen',date_pattern='dd/mm/yyyy')
    e4.place(x=250,y=170)
    
    bt=Button(t,text='Update',command=updatedata)
    bt.place(x=150,y=350)
    bt1=Button(t,text='Find',command=finddata)
    bt1.place(x=200,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
    
        
