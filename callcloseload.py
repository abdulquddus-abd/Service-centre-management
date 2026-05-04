import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcallcloseload():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='lightpink')
    def load():
        ta=Toplevel(t)
        ta.geometry('800x800')
        ta.title('load')
        ta.config(bg='lightpink')
        tt=Text(ta,width=80,height=30)
        tt.place(x=15,y=20)
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        msg=''
        sql="select * from callclose"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            msg=msg+str(r)+'\n'
        db.close()
        tt.insert(END,msg)
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        lt=[]
        sql="select callno from callclose"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            lt.append(r[0])
        db.close()
        e1['values']=lt
        
    heading=Label(t,text='Callclose find',bg='lightpink',fg='Black',font=('arial',20))
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
    
    l4=Label(t,text='Date of close',bg='lightpink')
    l4.place(x=50,y=170)
    e4=Entry(t,width=20)
    e4.place(x=250,y=170)
    
    bt=Button(t,text='Load',command=load)
    bt.place(x=350,y=350)
    msg=Label(t,text='',fg='red',font=('arial',15),bg='white')
    msg.place(x=100,y=450)
    filldata()
    t.mainloop()
    
    
        
