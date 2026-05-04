import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from servicecenterdashboard import *
from categorymasterdashboard import *
from productsdashboard import *
from servicetypedashboard import *
from staffdashboard import *
from engineersdashboard import *
from customerdashboard import *
from calldatadashboard import *
from callclosedashboard import *
from callfeedbackdashboard import *

t=tkinter.Tk()
t.geometry('500x500')
t.config(bg='sky blue')
t.title('new screen')

heading=Label(t,text='PROJECT SCM',bg='sky blue',fg='black',font=('arial',20))
heading.place(x=150,y=5)
bt1=Button(t,text='servicecenter',width=15,command=showservicecenterdashboard)
bt1.place(x=50,y=50)
bt2=Button(t,text='categorymaster',width=15,command=showcategorymasterdashboard)
bt2.place(x=50,y=90)
bt3=Button(t,text='products',width=15,command=showproductsdashboard)
bt3.place(x=50,y=130)
bt4=Button(t,text='servicetype',width=15,command=showservicetypedashboard)
bt4.place(x=50,y=170)
bt5=Button(t,text='staff',width=15,command=showstaffdashboard)
bt5.place(x=50,y=210)
bt6=Button(t,text='engineers',width=15,command=showengineersdashboard)
bt6.place(x=50,y=250)
bt7=Button(t,text='customer',width=15,command=showcustomerdashboard)
bt7.place(x=50,y=290)
bt8=Button(t,text='calldata',width=15,command=showcalldatadashboard)
bt8.place(x=50,y=330)
bt9=Button(t,text='callclose',width=15,command=showcallclosedashboard)
bt9.place(x=50,y=370)
bt10=Button(t,text='callfeedback',width=15,command=showcallfeedbackdashboard)
bt10.place(x=50,y=410)
t.mainloop()