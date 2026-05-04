import tkinter
import threading
import time
from tkinter import ttk
from tkinter import *

t=tkinter.Tk()
t.geometry('400x500')
t.title(' home screen ')

def progress():
    for i in range(1,101,1):
        time.sleep(0.1)
        a.config(text=i)
        Pr['valu']=i
        
def mx():
    ta=threading.Thread(target=progress)
    ta.start()
    
a=Label(t,text='Hello')
a.place(x=50,y=50)

Pr=ttk.Progressbar(t)
Pr.place(x=200,y=400)
   
bt1=Button(t,text=' Start ',command=mx)
bt1.place(x=150,y=400)

t.mainloop()