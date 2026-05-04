import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showservicetypesave():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='light pink')
    t.title('find screen')
    
    def savedata():
        if len(e1.get())==0: 
            msg.config(text='Pls fill Service_id')
        elif len(e2.get())==0: 
            msg.config(text='Pls fill Product id')
        elif len(e3.get())==0: 
            msg.config(text='Pls fill Cat_id')
        elif len(e4.get())==0: 
            msg.config(text='Pls fill Name')
        elif len(e5.get())==0: 
            msg.config(text='Pls fill Charges')
        elif len(e6.get())==0: 
            msg.config(text='Pls fill Duration days')
                  
        elif len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 or len(e6.get())==0:
            msg.config(text='Fill all data..')
        elif e5.get()<100:
            msg.config(text='Charges must be greater than 100')
        
        
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=int(e5.get())
            xf=int(e5.get())
            
            sql="insert into servicetype values('%s','%s','%s','%s',%d,%d)"%(xa,xb,xc,xd,xe,xf)
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
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select serviceid from servicetype"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt    
        
    heading=Label(t,text='Save st',bg='lightpink',fg='Black',font=('arial',20))
    heading.place(x=200,y=5)
    
    l1=Label(t,text='serviceid',bg='lightpink')
    l1.place(x=50,y=50)
    e1=ttk.Combobox(t)
    e1.place(x=250,y=50)
    
    l2=Label(t,text='prodid',bg='lightpink')
    l2.place(x=50,y=90)
    e2=Entry(t,width=20)
    e2.place(x=250,y=90)
    
    l3=Label(t,text='catid',bg='lightpink')
    l3.place(x=50,y=130)
    e3=Entry(t,width=20)
    e3.place(x=250,y=130)
    
    l4=Label(t,text='Name',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    l5=Label(t,text='Charges',bg='lightpink')
    l5.place(x=50,y=210)
    e5=Entry(t,width=20)
    e5.place(x=250,y=210)
    
    l6=Label(t,text='Durationdays',bg='lightpink')
    l6.place(x=50,y=250)
    e6=Entry(t,width=20)
    e6.place(x=250,y=250)

    bt=Button(t,text='save',command=savedata)
    bt.place(x=350,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
