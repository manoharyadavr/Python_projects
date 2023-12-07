from tkinter import *
from tkinter import messagebox

mw = Tk()
mw.title("ToDo List")
mw.geometry("600x400")
# mw.iconbitmap("todo.ico")
mw.resizable(height=False, width=False)

#creating a list to insert tasks into the List Box
tasks_list = []

def submit_btn():
    restult = input_box.get()
    if restult != "":
        task_list_box.insert(END, restult)
        input_box.delete(0,END)
    else:
        messagebox.showwarning("Warning","please enter a Task")

def delete():
    if task_list_box.curselection():
        task_list_box.delete(ANCHOR)
        messagebox.showinfo("Deleted", "Successfully deleted the task")
    else:
        pass

def edit_save():

    if input_box.get() != "":
        selected_task = task_list_box.curselection()
        # input_box.insert(0, task_list_box.anchor)
        result = input_box.get()
        task_list_box.insert(selected_task, result)
        task_list_box.delete(ANCHOR)
        input_box.delete(0, END)

        #submit task button
        submit = Button(mw, text="Submit", font="Arial, 14", padx=3, pady=3,
                 bg="#000000", fg="#ffffff", command=submit_btn)
        submit.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        messagebox.showinfo("info", "Edits are saved")

    else:
        messagebox.showwarning("warning", "type something to edit task")
        

def edit():

    if task_list_box.curselection():
        selected_index = task_list_box.curselection()
        selected_text = task_list_box.get(selected_index[0])
        input_box.delete(0, END)  # Clear the current content of the input_box
        input_box.insert(0, selected_text)

        edit_save_btn = Button(mw, text="   Edit   ", font="Arial, 14", padx=3,
                               pady=3, bg="#000000", fg="#ffffff", command=edit_save)
        edit_save_btn.grid(row=2, column=2, padx=10, pady=10, sticky=W)

    else:
        messagebox.showwarning("Waring", "Select a Task to edit")
        
#ToDo list label
todo_label = Label(
                    mw, text="ToDo List Application",
                    font=("Comic Sans MS", 20,"bold"),
                    width=35, height=2, bg="#07DE36", anchor="w",
                    padx=40
                 )
todo_label.grid(row=0, columnspan=3)

#input label
input_label = Label(mw, text="Add Items", font=("Javanese Text", 18))
input_label.grid(row=1, column=0, padx=10)

#input box
input_box = Entry(mw, font="Arial, 20")
input_box.grid(row=2, column=0, columnspan=2, padx=10, sticky=EW)

#submit task button
submit = Button(mw, text="Submit", font="Arial, 14", padx=3, pady=3,
                 bg="#000000", fg="#ffffff", command=submit_btn)
submit.grid(row=2, column=2, padx=10, pady=10, sticky=W)

#tasks heading
tasks_heading = Label(mw, text=" Tasks ", font=("Javanese Text", 18))
tasks_heading.grid(row=3, column=0, padx=10)

#list box to display the number of tasks
task_list_box = Listbox(mw, font="Arial, 15", height=4)
task_list_box.grid(row=4,padx=10, sticky=EW)

#scroll bar for the list box view
scrollbar = Scrollbar(mw, command=task_list_box.yview, width=20)
scrollbar.grid(column=1,row=4, sticky=NS)
task_list_box.config(yscrollcommand=scrollbar.set)

#buttons for the operations
frame = Frame(mw)
frame.grid(row=4, column=2, padx=5,sticky=EW)

edit_button = Button(frame, text=" Edit ", font="Arial, 13", padx=3,
                      pady=3,bg="#2ED400", fg="#ffffff", command=edit)
edit_button.grid(row=4, column=0, padx=5, pady=10)

delete_button = Button(frame, text="Delete", font="Arial, 13", padx=3,
                        pady=3, bg="#FF0F13", fg="#ffffff", command=delete)
delete_button.grid(row=4, column=1, padx=3, pady=10)


mw.mainloop()