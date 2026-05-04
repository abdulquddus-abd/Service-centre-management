import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from projectbuttons import *
t=tkinter.Tk()
t.geometry('1600x900')  
def login():
    ta=Toplevel(t)
    ta.geometry('400x400')
    ta.config(bg="burlywood")
    def check():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        sql="select count(*) from logintable where loginid='%s' and password='%s'"%(xa,xb)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            messagebox.showinfo('hi','failed')
        else:
            messagebox.showinfo('verified','welcome')
            showprojectbuttons()
        db.close()
        
    def sendmail():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        sql="select password,email from logintable where loginid='%s'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        password=data[0]
        mail=data[1]
        db.close()
        from_address = "abdulquddusbaig5@gmail.com"
        to_address = mail
        messagebox.showinfo('hi','Password send to your mailid')
    
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Your Password"
        msg['From'] = from_address
        msg['To'] = to_address
    
        # Create the message (HTML).
        
        Text ="password is <br>"+password
    
        # Record the MIME type - text/html.
        part1 = MIMEText(Text, 'html')
    
        # Attach parts into message container
        msg.attach(part1)
    
        # Credentials
        username = 'abdulquddusbaig5@gmail.com'  
        password = 'qxredgweakpftkjl'
    
        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
    e1=Entry(ta,width=20,bg='skyblue')
    e1.insert(0,'lOGINID')
    e1.place(x=145,y=70)

    e2=Entry(ta,width=20,bg='skyblue')
    e2.insert(0,'PASSWORD')
    e2.place(x=145,y=120)
    btt=Button(ta,text='LOGIN',command=check,bg='blue',fg='white')
    btt.place(x=110,y=225)
    bt1=Button(ta,text='FORGOT PASSWORD',command=sendmail,bg='red',fg='white')
    bt1.place(x=220,y=225)
def signup():
    tb=Toplevel(t)
    tb.geometry('400x400')
    tb.config(bg='darkorange')
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='scm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        sql="insert into logintable values('%s','%s','%s')"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','saved')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        
    heading=Label(t,text='Login table',bg='lightgrey',fg='Black',font=('arial',20))
    heading.place(x=170,y=5)
    
    e1=Entry(tb,width=20)
    e1.insert(0,'Fill   Loginid')
    e1.place(x=135,y=50)

    e2=Entry(tb,width=20,show='*')
    e2.insert(0,'Fill   Password')
    e2.place(x=135,y=90)

    e3=Entry(tb,width=20)
    e3.insert(0,'Fill   Emailid')
    e3.place(x=135,y=130)

    bt=Button(tb,text='Save',command=savedata)
    bt.place(x=150,y=300)
    bt=Button(tb,text='Close')
    bt.place(x=250,y=300)
    tb.mainloop()

img=PhotoImage(master=t,file='C:/Users/Dell/OneDrive/Pictures/Documents/AFHJFG.png')
me=Label(t,image=img)
me.place(x=0,y=0)

bt=Button(t,text='Signin',command=login,bg='black',fg='white')
bt.place(x=35,y=70)
bt1=Button(t,text='Signup',command=signup,bg='black',fg='white')
bt1.place(x=35,y=130)

t.mainloop()