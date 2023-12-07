#importing random module to generate random letters, numbers, and symbols
#importing tkinter module for the GUI interface 
import random
from tkinter import *
from tkinter import messagebox

mw = Tk()
mw.title("Password Generator")
mw.geometry("900x600")
mw.resizable(height=False, width=False)
# mw.iconbitmap("password.ico")

label = Label(mw, text="Password Generator", fg="#0000cc", font=("Arial", 30, "bold", "underline"))
label.grid(column=0, row=0, padx=160, pady=50)

#creating a method to generate password 
def generate_password():

    try:
        chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
                'q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
                'Q','R','S','T','U','V','W','X','Y','Z',
                '0','1','2','3','4','5','6','7','8','9','!','@','#','$','&','*']
        password = ""
        get_password.delete(0,END)
        for i in range(int(get_len.get())):

            password += random.choice(chars)
        
        get_password.insert(0, password)

    except:
        if get_name.get() == "":
            messagebox.showwarning("empty name", "please enter your name")
        else:
            messagebox.showwarning("Warning", "password length can't be empty or string")


#creating a method to close the window when user click the accpt button
def accept_password():
    exit()


#creating a method to empty the all details entered by the user when user clicks the reset button
def reset_password():
    get_name.delete(0,END)
    get_len.delete(0,END)
    get_password.delete(0,END)


#created a frame to insert name, password length and generated password fields so that it wont be 
#get diffused 
frame = Frame(mw)
frame.grid(column=0, row=1, padx=90)

#displaying the Enter user name label
name = Label(frame, text="Enter user Name: ", padx=20, font=("Arial", 20))
name.grid(column=0, row=1, sticky=E, padx=10, pady=10)

#taking the input for name field the user
get_name = Entry(frame, width=20, font=("Arial",20))
get_name.grid(column=1, row=1, sticky=E, padx=10, pady=10)

#displaying the password length label
password_len = Label(frame, text="Enter password length: ", padx=10, font=("Arial", 20))
password_len.grid(column=0, row=2, sticky=E, padx=10, pady=10)

#taking the input for length of the password field the user
get_len = Entry(frame, width=20, font=("Arial",20))
get_len.grid(row=2, column=1, sticky=E, padx=10, pady=10)

#Displaying the generated password
generated_password = Label(frame, text="Generated Password: ",padx=10, font=("Arial", 20), bd=1)
generated_password.grid(column=0, row=3, sticky=E, padx=10, pady=10)

#Displaying the generated password for the user
get_password = Entry(frame, width=20, font=("Arial",20))
get_password.grid(row=3, column=1, sticky=E, padx=10, pady=10)

#creating a button to generate the password
generate_btn = Button(mw, text="GENERATE PASSWORD", font="Arial, 20", fg="#ffffff", 
                      background="#0000cc", border=4, command=generate_password)
generate_btn.grid(row=2, column=0, padx=90, pady=15)

#creating a button to generate the password
generate_btn = Button(mw, text="ACCEPT", font="Arial, 20", fg="#0000cc", 
                      background="#ffffff", border=3, command=accept_password)
generate_btn.grid(row=3, column=0, padx=90, pady=10)

#creating a button to generate the password
generate_btn = Button(mw, text="RESET", font="Arial, 20", fg="#0000cc", 
                      background="#ffffff", border=3, command=reset_password)
generate_btn.grid(row=4, column=0, padx=90, pady=10)


#main loop is used to stay the window until we close
mw.mainloop()
