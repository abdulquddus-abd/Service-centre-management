import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
from tkinter import PhotoImage
from callfeedbacksave import *
from callfeedbackfind import *
from callfeedbackdelete import *
from callfeedbackload import *
from callfeedbackupdate import *
from callfeedbacknavigate import *
def showcallfeedbackdashboard():
    t=tkinter.Tk()
    t.geometry('1500x900')
    t.config(bg='#E6E9EE')
    t.title('Call feedback')
    
    heading=Label(t,text='CALL FEEDBACK',bg='#E6E9EE',fg='black',font=('arial',40))
    heading.place(x=500,y=5)
    bt1=Button(t,text='Save',width=30,height=5,bg='#F0F2F5',command=showcallfeedbacksave)
    bt1.place(x=50,y=50)
    bt2=Button(t,text='Delete',width=30,height=5,bg="lightgrey",command=showcallfeedbackdelete)
    bt2.place(x=50,y=150)
    bt3=Button(t,text='Find',width=30,height=5,bg="#DDE3EA",command=showcallfeedbackfind)
    bt3.place(x=50,y=250)
    bt4=Button(t,text='Update',width=30,height=5,bg="#E3E7ED",command=showcallfeedbackupdate)
    bt4.place(x=50,y=350)
    bt5=Button(t,text='show',width=30,height=5,bg="#EAECEF",command=showcallfeedbackload)
    bt5.place(x=50,y=450)
    bt6=Button(t,text='Navigate',width=30,height=5,bg="#E8EDF3",command=showcallfeedbacknavigate)
    bt6.place(x=50,y=550)
    img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Documents/AQ spyder project/feedbackimage.png')
    me=Label(t,image=img,bg='#E6E9EE')
    me.place(x=400,y=100)
    t.mainloop()