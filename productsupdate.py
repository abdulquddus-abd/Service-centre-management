import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showproductsupdate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    t.title('find screen')
    
    def finddata():
        if len(e1.get())==0:
            msg.config(text='Pls Fill Prodid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select prodid,catid,pname,warrantyyears,remarks from products where prodid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            
            e2.insert(0,data[1])
            e3.insert(0,data[2])
            e4.insert(0,data[3])
            e5.insert(0,data[4])
            
            
            db.close()
            msg.config(text='Data founded')
    
    def updatedata():
        if xe == "" or xe == "0" or xe<1 or xe>5:
            msg.config(text='Error, Invalid remark')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            sql="update products set catid='%s',pname='%s',warrantyyears=%d,remarks='%s' where prodid='%s'"%(xb,xc,xd,xe,xa)
            cur.execute(sql)
            db.commit()
            db.close()
            msg.config(text='Data Updated,Thanks')
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
        
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
        
    heading=Label(t,text='Update products',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=160,y=5)
    
    l1=Label(t,text='Prodid',bg='lightpink')
    l1.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=250,y=50)
    
    l2=Label(t,text='Catid',bg='lightpink')
    l2.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    
    l3=Label(t,text='Pname',bg='lightpink')
    l3.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=250,y=130)
    
    l4=Label(t,text='Warranty years',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    l5=Label(t,text='Remarks',bg='lightpink')
    l5.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=250,y=210)
    
    bt=Button(t,text='Update',command=updatedata)
    bt.place(x=150,y=300)
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=250,y=300)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
