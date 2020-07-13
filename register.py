from tkinter import *
import os

def register_user():
    username_info  = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    #clear the fields
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text = "Registration Success", fg = "green", font = ("calibri, 11")).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Password * ").pack()    
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = "10", height = "1", command = register_user).pack()

def delete3():
    screen3.destroy()


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text = "").pack()
    Label(screen3, text = "Login Success").pack()
    Button(screen3, text = "OK", command = delete3).pack()

def delete4():
    screen4.destroy()

def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password Not Recognized")
    screen4.geometry("150x100")
    Label(screen4, text = "").pack()
    Label(screen4, text = "Password Error").pack()
    Button(screen4, text = "OK", command = delete4).pack()

def delete5():
    screen5.destroy()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    Label(screen5, text = "").pack()
    screen5.title("User Not Found")
    screen5.geometry("150x100")
    Label(screen5, text = "User Not Found Error").pack()
    Button(screen5, text = "OK", command = delete5).pack()



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry2.delete(0, END)
    password_entry2.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files: 
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            # print("login success!")
            login_success()
        else:
            # print("password has not been recognized")
            password_not_recognized()
    else:
        # print("User not found!")
        user_not_found()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry2  #Login infor
    global password_entry2  #Login infor

    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Username * ").pack()
    username_entry2 = Entry(screen2, textvariable = username_verify)
    username_entry2.pack()
    Label(screen2, text = "").pack()
    username_entry2.pack()
    Label(screen2, text = "Password * ").pack()    
    password_entry2 = Entry(screen2, textvariable = password_verify)
    password_entry2.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = "300", height="2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width="30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width="30", command = register).pack()
    Label(text = "").pack()

    screen.mainloop()

main_screen()
