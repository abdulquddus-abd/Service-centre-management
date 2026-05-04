import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showcallfeedbacksave():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('find screen')
    
    def savedata():
        if len(e1.get())==0:
            msg.config('Fill callno pls')
        elif len(e2.get())==0:
            msg.config('Fill custid pls')
        elif len(e3.get())==0:
            msg.config('Fill Eng_id pls')
        elif len(e4.get())==0:
            msg.config('Fill Ratings pls')
        elif len(e5.get())==0:
            msg.config('Fill Remarks pls')
        elif len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0:
            msg.config(text='Fill all data..')
        elif int(e4.get())<1 or int(e4.get())>5:
            msg.config(text='Invalid ratings')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=int(e4.get())
            xe=e5.get()
            if xe == "" or xe == "0":
                msg.config(text='Error, Invalid remark')
            else:
                sql="insert into callfeedback values('%s','%s','%s',%d,'%s')"%(xa,xb,xc,xd,xe)
                cur.execute(sql)
                db.commit()
                db.close()
                msg.config(text='Data saved,Thanks')
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
           
        
    heading=Label(t,text='Call feedback save',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=170,y=5)
    l1=Label(t,text='Call no',bg='lightpink')
    l1.place(x=50,y=50)
    e1=Entry(t,width=20)
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
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=350,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    
    t.mainloop()
    
    
        