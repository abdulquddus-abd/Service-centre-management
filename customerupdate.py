import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcustomerupdate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('find screen')
    
    def finddata():
        if len(e1.get())==0:
            msg.config(text='Pls Fill Serviceid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select custid,name,phone,email,address,catid,prodid,dateofpurchase from customer where custid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
            e7.delete(0,END)
            e8.delete(0,END)
           
            e2.insert(0,data[1])
            e3.insert(0,data[2])
            e4.insert(0,data[3])
            e5.insert(0,data[4])
            e6.insert(0,data[5])
            e7.insert(0,data[6])
            e8.insert(0,data[7])
            
            db.close()
            msg.config(text='Data founded')
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        xg=e7.get()
        xh=e8.get()
        sql="update customer set name='%s',phone='%s',email='%s',address='%s',catid='%s',prodid='%s',dateofpurchase='%s' where custid='%s'"%(xb,xc,xd,xe,xf,xg,xh,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        msg.config(text='Data Updated,Thanks')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select custid from customer"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt    
        
    heading=Label(t,text='Customer update',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=170,y=5)
    l1=Label(t,text='Cust id',bg='lightpink')
    l1.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=250,y=50)
    
    l2=Label(t,text='Name',bg='lightpink')
    l2.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    
    l3=Label(t,text='Phone',bg='lightpink')
    l3.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=250,y=130)
    
    l4=Label(t,text='Email',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    l5=Label(t,text='Address',bg='lightpink')
    l5.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=250,y=210)
    
    l6=Label(t,text='Catid',bg='lightpink')
    l6.place(x=50,y=250)
    e6=Entry(t,width=20)
    e6.place(x=250,y=250)
    
    l7=Label(t,text='Prodid',bg='lightpink')
    l7.place(x=50,y=290)
    e7=Entry(t,width=20)
    e7.place(x=250,y=290)
    
    l8=Label(t,text='Date of purchase',bg='lightpink')
    l8.place(x=50,y=330)
    e8=Entry(t,width=20)
    e8.place(x=250,y=330)
    
    bt=Button(t,text='Find',command=finddata)
    bt.place(x=350,y=350)
    bt1=Button(t,text='Update',command=updatedata)
    bt1.place(x=150,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
    
        
