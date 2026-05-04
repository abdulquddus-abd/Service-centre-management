import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showcategorymasterupdate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    t.title('find screen')
    def finddata():
        if len(e1.get())==0:
            msg.config(text='Pls Fill Serviceid')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="select catid,catname,remarks from categorymaster where catid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            e2.delete(0,END)
            e3.delete(0,END)
           
           
            e2.insert(0,data[1])
            e3.insert(0,data[2])
        
        db.close()
        msg.config(text='Data founded')
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        if xc == "" or xc == "0":
            msg.config(text='error,invalid remark')
        else:
            msg.config(text='error,invalid remark')
        sql="update categorymaster set catname='%s',remarks='%s' where catid='%s'"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        msg.config(text='Data Updated,Thanks')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
       
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select catid from categorymaster"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt   
        
        
        
    heading=Label(t,text='Update cm',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=160,y=5)
    l1=Label(t,text='catid',bg='lightpink')
    l2=Label(t,text='catname',bg='lightpink')
    l3=Label(t,text='remarks',bg='lightpink')
    
    l1.place(x=50,y=50)
    l2.place(x=50,y=90)
    l3.place(x=50,y=130)
    
    
    e1=ttk.Combobox(t)
    e2=Entry(t,width=20)
    e3=Entry(t,width=20)
    
    e1.place(x=250,y=50)
    e2.place(x=250,y=90)
    e3.place(x=250,y=130)
    
    
    bt=Button(t,text='update',command=updatedata)
    bt.place(x=250,y=300)
    bt1=Button(t,text='find',command=finddata)
    bt1.place(x=150,y=300)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
