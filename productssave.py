import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showproductssave():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    t.title('find screen')
    
    def savedata():
        if len(e1.get())==0:
            msg.config(text='Fill prod_id pls')
        elif len(e2.get())==0:
            msg.config(text='Fill cat_id pls')
        elif len(e3.get())==0:
            msg.config(text='Fill product name pls')
        elif len(e4.get())==0:
            msg.config(text='Fill warranty years pls')
        elif len(e5.get())==0:
            msg.config(text='Fill remarks pls')
            
        elif len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
            msg.config(text='Fill all data..')
            
        elif e5 == "" or e5 == "0" or e5<1 or e5>5:
            msg.config(text='Error, Invalid remark')
        elif e4<1:
            msg.config(text='Warranty years must be greater than one')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=int(e4.get())
            xe=e5.get()
           
            sql="insert into products values('%s','%s','%s',%d,'%s')"%(xa,xb,xc,xd,xe)
            cur.execute(sql)
            db.commit()
            db.close()
            msg.config(text='Data Saved,Thanks')
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
            e5.delete(0,END)
            e6.delete(0,END)
        
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
        
    heading=Label(t,text='Save products',bg='lightpink',fg='Black',font=('arial',20))
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
    
    bt=Button(t,text='save',command=savedata)
    bt.place(x=150,y=300)
    
    filldata()
    t.mainloop()
