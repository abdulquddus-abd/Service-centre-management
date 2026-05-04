import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showcategorymastersave():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    t.title('service center')
    
   
    def savedata():
        if len(e1.get())==0:
            msg.config(text='Fill catid pls')
        elif len(e2.get())==0:
            msg.config(text='Fill catname pls')
        elif len(e3.get())==0:
            msg.config(text='Fill Remarks pls')
        elif len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0:
            msg.config(text='Fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            if xc == "" or xc == "0":
                msg.config(text='Error, Invalid remark')
            else:
                sql="insert into categorymaster values('%s','%s','%s')"%(xa,xb,xc)
                cur.execute(sql)
                db.commit()
                db.close()
                msg.config(text='Hi,saved')
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
    heading=Label(t,text='Save cm',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=160,y=5)
    l1=Label(t,text='catid',bg='lightpink')
    l1.place(x=50,y=50)
    l2=Label(t,text='catname',bg='lightpink')
    l2.place(x=50,y=90)
    l3=Label(t,text='remarks',bg='lightpink')
    l3.place(x=50,y=130)
    
    e1=Entry(t,width=20)
    e1.place(x=250,y=50)
    
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    e3=Entry(t,width=20)
    
    e3.place(x=250,y=130)
    
    
    bt1=Button(t,text='save',command=savedata)
    bt1.place(x=150,y=300)
    
    
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
