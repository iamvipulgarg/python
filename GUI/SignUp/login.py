from tkinter import *
import mysql.connector
import hashlib

def connectDB():
    return mysql.connector.connect(host="localhost",port="3306",user="root",password="",db="py_tkinter")
    
def checkCreds(userID,pwd):
    # con=mysql.connector.connect(host="localhost",port="3306",user="root",password="",db="py_tkinter")
    con=connectDB()
    cur= con.cursor()
    sel = "select * from users where username = '{}' AND password = '{}'".format(userID,hashlib.sha256(pwd.encode()).hexdigest())
    # sel = "select * from users where username = '{}' AND id = '{}'".format(userID,pwd)
    cur.execute(sel)
    data=cur.fetchall()
    cur.close()
    con.close()
    if data:
        return True;
    else :
        return False;

def login():
    userID=e1.get()
    pwd=e2.get()
    if userID != '' and pwd !='' :
        if checkCreds(userID,pwd):
            e1.delete(0,END)
            e2.delete(0,END)
            status_label.config(text="Successfully Logged in")
        else:
            status_label.config(text="Incorrect Creds")
    else:
        status_label.config(text='Enter User Name or Password')
    
def register():
    top=Toplevel()
    top.geometry("350x350")
    top.title('Sign Up')
    
    lb5=Label(top,text="User Name")
    lb5.grid(row=0,column=0)
    e5=Entry(top)
    e5.grid(row=0,column=1)
    lb6=Label(top,text="Password")
    lb6.grid(row=1,column=0)
    e6=Entry(top)
    e6.grid(row=1,column=1)
    lb7=Label(top,text="City")
    lb7.grid(row=2,column=0)
    e7=Entry(top)
    e7.grid(row=2,column=1)
    def store():
        con=mysql.connector.connect(host="localhost",port="3306",user="root",password="",db="py_tkinter")
        cur= con.cursor()
        username=e5.get()
        pwd=hashlib.sha256(e6.get().encode()).hexdigest()
        city=e7.get()
        sel="insert into users (username,password,city) values('{}','{}','{}')".format(username,pwd,city)
        cur.execute(sel)
        con.commit()
        top.destroy()
    
    b5=Button(top,text='Sign Up',command=store)
    b5.grid(row=3,column=3)
    
    
root = Tk()
root.geometry("700x700")
root.title("Login")

status_label = Label(root, text="", font=("Arial", 10))
status_label.place(x=250, y=10)

lb1= Label(text="User Name")
lb1.grid(row=0,column=0)

e1 = Entry()
e1.grid(row=0,column=1)

lb2=Label(text="password")
lb2.grid(row=1,column=0)

e2=Entry()
e2.grid(row=1,column=1)

b1=Button(text="Login",command=login)
b1.grid(row=2,column=0)

b2=Button(text="Register",command=register)
b2.grid(row=2,column=1)

l3=Label(text='')
l3.grid(row=3,column=0)

root.mainloop()