from tkinter import *

#main window for the calculator
mw = Tk()
mw.title("Calculator")
# mw.iconbitmap("calculator.ico")
mw.resizable(width=False, height=False)

#method to appear number in the screen
def click(num):
   current_num = entry.get()
   entry.delete(0,END)
   f_num = current_num + num
   entry.insert(0, f_num)

first_num = 0
math=""

#method to perform the calculations when user clicks on the mathematical symbols
def calculation(calc):
    global first_num, math
    math = calc
    first_num = entry.get()
    entry.insert(END, calc)
    
#method to perform the calculations when user clicks equals symbol and displays output
def equals():
    global first_num, math
    
    second_num = entry.get().replace(str(first_num)+math, "")
    entry.delete(0, END)

    if math == "+":    
        result = float(first_num) + float(second_num)
        result = round(result, 3)

    elif math == "*":
        result = float(first_num) * float(second_num)
        result = round(result, 3)

    elif math == "^":
        result = float(first_num) ** float(second_num)
        result = round(result, 3)

    elif math == "√":
        if first_num == "":
            first_num = "1"
        result = float(second_num) ** 0.5
        result = round(result, 3)

    elif math == "-":
        result = float(first_num) - float(second_num)
        result = round(result, 3)

    elif math == "/":
        try:
            result = float(first_num) / float(second_num)
            result = round(result, 3)
        except ZeroDivisionError:
            result = "ZeroDivisionError"

    elif math == ".":
        result = entry.get().replace(str(first_num)+math, "")
        

    elif math == "+-":
        result = -float(first_num)

    else:
        result = entry.get()

    entry.insert(0, result)

#input box for the calculator from here the data will be displayed to the user
entry = Entry(mw,width=15, font=("Arial", 28), justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4,padx=10,pady=10)


# all buttons are creating and adding to the calculator by using grid method
btn_9 = Button(mw, text="9",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : click("9"))
btn_9.grid(row=2, column=2, padx=2, pady=2)

btn_8 = Button(mw, text="8",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : click("8"))
btn_8.grid(row=2, column=1, padx=2, pady=2)

btn_7= Button(mw, text="7",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : click("7"))
btn_7.grid(row=2, column=0, padx=2, pady=2)

btn_6= Button(mw, text="6", font="Arial, 15 bold" ,padx=36, pady=10, command=lambda : click("6"))
btn_6.grid(row=3, column=2, padx=2, pady=2)

btn_5= Button(mw, text="5", font="Arial, 15 bold" ,padx=36, pady=10, command=lambda : click("5"))
btn_5.grid(row=3, column=1, padx=2, pady=2)

btn_4= Button(mw, text="4", font="Arial, 15 bold" ,padx=36, pady=10, command=lambda : click("4"))
btn_4.grid(row=3, column=0, padx=2, pady=2)

btn_3 = Button(mw, text="3",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : click("3"))
btn_3.grid(row=4, column=2, padx=2, pady=2)

btn_2 = Button(mw, text="2",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : click("2"))
btn_2.grid(row=4, column=1, padx=2, pady=2)

btn_1 = Button(mw, text="1",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : click("1"))
btn_1.grid(row=4, column=0, padx=2, pady=2)

btn_0 = Button(mw, text="0",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : click("0"))
btn_0.grid(row=5, column=1, padx=2, pady=2)


#calculations buttons are creating and adding to the main window by using grid method
btn_clear = Button(mw, text="C",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : entry.delete(0,END))
btn_clear.grid(row=1, column=0, padx=2, pady=2)

btn_sqrt = Button(mw, text="√",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : calculation("√"))
btn_sqrt.grid(row=1, column=1, padx=2, pady=2)

btn_div = Button(mw, text="/",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : calculation("/"))
btn_div.grid(row=1, column=2, padx=2, pady=2)

btn_neg = Button(mw, text="+-",font="Arial, 15 bold" , padx=33, pady=10, command=lambda : calculation("+-"))
btn_neg.grid(row=1, column=3, padx=2, pady=2)

btn_mul = Button(mw, text="*",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : calculation("*"))
btn_mul.grid(row=2, column=3, padx=2, pady=2)

btn_add = Button(mw, text="+",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : calculation("+"))
btn_add.grid(row=3, column=3, padx=2, pady=2)

btn_sub = Button(mw, text="-", font="Arial, 15 bold" ,padx=36, pady=10, command=lambda : calculation("-"))
btn_sub.grid(row=4, column=3, padx=2, pady=2)

btn_pow = Button(mw, text="^",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : calculation("^"))
btn_pow.grid(row=5, column=0, padx=2, pady=2)

#Equals to button
btn_equals = Button(mw, text="=",font="Arial, 15 bold" , padx=36, pady=10, command=equals)
btn_equals.grid(row=5,column=3, padx=2, pady=2)

btn_mod = Button(mw, text=".",font="Arial, 15 bold" , padx=36, pady=10, command=lambda : calculation("."))
btn_mod.grid(row=5,column=2, padx=2, pady=2)


#main loop is user to stay the calculator window until we close
mw.mainloop()