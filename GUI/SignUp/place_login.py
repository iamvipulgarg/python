from tkinter import *


root = Tk()
root.geometry("400x400")
root.title("Login")

Label(text="Enter User Name : ").place(x=50,y=50)
Entry().place(x=200,y=50)

Label(text="Enter Password : ").place(x=50,y=75)
Entry().place(x=200,y=75)

Button(text="Login").place(x=50,y=100)
Button(text="Register").place(x=200,y=100)

root.mainloop()