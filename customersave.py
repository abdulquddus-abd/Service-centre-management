import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from tkcalendar import DateEntry
def showcustomersave():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('find screen')
    def savedata():
        email=e4.get()
        if len(e1.get())==0: 
            msg.config(text='Pls fill Cust_id')
        elif len(e2.get())==0: 
            msg.config(text='Pls fill Name')
        elif len(e3.get())==0: 
            msg.config(text='Pls fill Phone')
        elif len(e4.get())==0: 
            msg.config(text='Pls fill Email')
        elif len(e5.get())==0: 
            msg.config(text='Pls fill Address')
        elif len(e6.get())==0: 
            msg.config(text='Pls fill Cat_id')
        elif len(e7.get())==0: 
            msg.config(text='Pls fill Prod_id')
        elif len(e8.get())==0: 
            msg.config(text='Pls fill Date of purchase')
            
        elif len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or len(e6.get())==0 or len(e7.get())==0 or len(e8.get())==0:
            msg.config(text='fill all data..')
        elif len(e3.get())!=10:
            msg.config(text='Invalid phone no.')
        elif email.count('@')!=1:
            msg.config(text='Invalid Email id')
        else:
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
            sql="insert into customer values('%s','%s','%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg,xh)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','saved')
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
        
    heading=Label(t,text='customers save',bg='lightpink',fg='Black',font=('arial',20))
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
    e8=DateEntry(t,width=15,bg='lightpink',date_pattern='dd/mm/yyyy')
    e8.place(x=250,y=330)
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=200,y=400)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
    
        