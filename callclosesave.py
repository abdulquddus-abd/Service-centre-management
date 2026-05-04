import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from datetime import datetime
def showcallclosesave():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('Save screen')
    
    def savedata():
        
        if len(e1.get())==0: 
            msg.config(text='Pls fill Call no')
        elif len(e2.get())==0: 
            msg.config(text='Pls fill Cust_id')
        elif len(e3.get())==0: 
            msg.config(text='Pls fill Eng_id')
        elif len(e4.get())==0: 
            msg.config(text='Pls fill Date of close')
        
            
        elif len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            msg.config(text='fill all data..')
            
        else:
       
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            sql="insert into callclose values('%s','%s','%s','%s')"%(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            msg.config(text='Hi,saved')
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
    
    
        
    heading=Label(t,text='Callclose saves',bg='lightpink',fg='Black',font=('arial',20))
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
    
    l4=Label(t,text='Date of close',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    dt=datetime.now().strftime("%d-%m-%Y")
    e4.insert(0,dt)
    e4.place(x=250,y=170)
    
    bt=Button(t,text='Save',command=savedata)
    bt.place(x=350,y=350)
    
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    t.mainloop()
    
    
        
