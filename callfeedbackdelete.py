import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcallfeedbackdelete():

    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title(' screen')
    
    def delete():
        if len(xa.get())==0:
            msg.config(text='Pls fill callno')
        if len(xb.get())==0:
            msg.config(text='Pls fill Custid')
        if len(xc.get())==0:
            msg.config(text='Pls fill Engid')
        if len(xd.get())==0:
            msg.config(text='Pls fill Ratings')
        if len(xe.get())==0:
            msg.config(text='Pls fill Remarks')
        else:
                        
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            sql="delete from callfeedback where callno='%s'"%(xa)
            cur.execute(sql)
            db.commit()
            db.close()
            msg.config(text='Data Deleted,Thanks')
            e1.delete(0,END) 
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select callno from callfeedback"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt    
        
    heading=Label(t,text='Call feedback delete',bg='lightpink',fg='Black',font=('arial',20))
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
    
    l4=Label(t,text='Ratings',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    l5=Label(t,text='Remarks',bg='lightpink')
    l5.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=250,y=210)
    
    bt=Button(t,text='Delete',command=delete)
    bt.place(x=350,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
    
        