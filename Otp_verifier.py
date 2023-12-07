from twilio.rest import Client
from tkinter import *
from tkinter import messagebox
import random


account_sid = "ACd74b3b35aadd75ea01b8a7e65af35244"
auth_token = "e213d16bd62fd762f581b46bfa5525e0"
my_mobile_no = "+17169346125"


def submit_num():
    send_otp(number_entry.get(), generated_otp)

def otp_verification():
    verify_otp()


root = Tk()
root.title("OTP Verification System")
root.geometry("600x400")

title_label = Label(root, text="Verify your OTP", font=("Arial", 20, "bold"), foreground="#B31312")
title_label.grid(row=0, column=1)

number_label = Label(root, text="Enter your Number: ", font=("Arial", 15))
number_label.grid(row=1, column=0, padx=30)

number_entry = Entry(root, font=("Arial", 15))
number_entry.grid(row=1, column=1)

submit_btn = Button(root, text="Submit", font=("Arial", 15), background="#2B2A4C", fg="#ffffff", command=submit_num)
submit_btn.grid(row=2, column=1, pady=10)

otp_label = Label(root, text="Enter your OTP:", font=("Arial", 15))
otp_label.grid(row=3, column=0)

otp_entry = Entry(root, font=("Arial", 15))
otp_entry.grid(row=3, column=1)

otp_submit = Button(root, text="Submit", font=("Arial", 15), background="#2B2A4C", fg="#ffffff", command=otp_verification)
otp_submit.grid(row=4, column=1, pady=10)



def Gen_otp():
    return str(random.randint(1000, 9999))

generated_otp = Gen_otp()



def send_otp(mobile_no, otp):
    try:
        
            client = Client(account_sid, auth_token)    
            messsage = client.messages.create(to=mobile_no, from_=my_mobile_no, body=f"Your OTP is: {otp}")
            
    except:
            if number_entry.get() != "":            
                messagebox.showwarning("Invalid", "Please Enter a proper Mobile Number..!")


def verify_otp():
    otp_verification = otp_entry.get()
    if otp_verification == generated_otp:
        messagebox.showinfo("Verification Successful", "OTP verification is Successfull, welcome to our application.")
    elif otp_verification != generated_otp and "":
        messagebox.showwarning("Verification Unsuccessful", "Please check OTP and Re-Enter")


root.mainloop()