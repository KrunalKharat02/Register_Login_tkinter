# My first register login interface in tkinter

from tkinter import *
import os
from tkinter import messagebox

def login_sucess():
    screen3=Toplevel(screen)
    screen3.geometry("250x200")
    screen3.title("Sucess")
    Label(screen3,text="Login Succesful").pack()
    Button(screen3,text="OK",command=screen3.destroy).pack()

def password_incorrect():
    screen3 = Toplevel(screen)
    screen3.geometry("250x200")
    screen3.title("WARNNING")
    Label(screen3, text="Incoorect Password").pack()
    Button(screen3, text="Try Again", command=screen3.destroy).pack()
def user_not_found():
    screen3 = Toplevel(screen)
    screen3.geometry("250x200")
    screen3.title("USER NOT FOUND")
    Label(screen3, text="User Not Found").pack()
    Button(screen3, text="OK", command=screen3.destroy).pack()




def Login_user():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    list_of_files = os.listdir()
    if len(username1) != 0 and len(password1) != 0:
        if username1 in list_of_files:
            file1 = open(username1,"r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
            else:
                password_incorrect()

        else:
            user_not_found()
    else:
        if len(username1) == 0:
            messagebox.showwarning("ERROR","Username can't be empty")
        else:
            messagebox.showwarning("ERROR", "Password can't be empty")







def Login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.geometry("300x280")
    screen2.title("Login")
    global username_entry1
    global password_entry1
    global username_verify
    global password_verify
    username_verify= StringVar()
    password_verify= StringVar()
    Label(screen2, text="Please Fill Up The Information To Login: ").pack()
    Label(screen2,text = "").pack()
    Label(screen2, text="Username * ", height="2", width="25").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ", height="2", width="25").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2,text="Login",command=Login_user,bg="lightblue",width="10",height="1").pack()
    Button(screen2, text="Create Account", command=Register, width="15", height="1").pack(side="left")





def Register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1,text="Registration Success", fg="green").pack()

def Register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("300x280")
    screen1.title("Register")
    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1,text ="Please Fill Up The Information: ").pack()
    Label(screen1,text = "").pack()
    Label(screen1,text ="Username * ",height ="2", width = "25").pack()
    username_entry=Entry(screen1,textvariable = username)
    username_entry.pack()
    Label(screen1,text = "").pack()
    Label(screen1, text="Password * ", height="2", width="25").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register",command = Register_user,bg = "lightblue",height="1",width ="10").pack()
    Button(screen1,text="Already an user",command= Login,width="15",height="1").pack(side="left")


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x280")
    screen.title("My Program")
    Label(text ="My Program" ,bg="grey",width = "300", height ="2"  ,font ="Calibri 15").pack()
    Label(text = "").pack()
    Button(text = "Register",width= "30",height = "2",command=Register).pack()
    Label(text = "").pack()
    Button(text = "Login",width= "30",height = "2",command=Login).pack()

    screen.mainloop()

main_screen()

