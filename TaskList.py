from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('tasks.db')

# define functions

# Add stuff to listbox
def populate_list():
    TaskList_list.delete(0, END)
    for row in db.fetch():
        TaskList_list.insert(END, row)


# Add Task
def add_task():
    if TaskList_text.get() == '':
     messagebox.showerror('You did not input any task!')
     return
    db.insert(TaskList_text.get())
    TaskList_list.delete(0, END)
    TaskList_list.insert(END, (TaskList_text.get()))
    clear_tasks()
    populate_list()

# remove Tasks
def remove_task():
    db.remove(selected_item[0])
    clear_tasks()
    populate_list()


# Clear Tasks
def clear_tasks():
    TaskList_entry.delete(0, END)

# Select item from textbox
def select_item(event):
    try:
        global selected_item
        index = TaskList_list.curselection()[0]
        selected_item = TaskList_list.get(index)

        TaskList_entry.delete(0, END)
        TaskList_entry.insert(END, selected_item[1])
    except IndexError:
        pass

# Create window
Prog = Tk()

# Program stuff
Prog.title('TaskList')
Prog.geometry('700x400')
Prog.resizable(width=False, height=False)

# Widgets
TaskList_text = StringVar()
TaskList_label = Label(Prog, text='Task:', font=('bold', 14), pady=20, padx=10)
TaskList_label.grid(row=0, column=0, sticky=W)
TaskList_entry = Entry(Prog, textvariable=TaskList_text, borderwidth = 1, width="50")
TaskList_entry.grid(row=0, column=1)

# Task list (Listbox)
TaskList_list = Listbox(Prog, height=15, width=100, border=0)
TaskList_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=10)

# Scrollbar
Scrollbar = Scrollbar(Prog)
Scrollbar.grid(row=4, column=3)

# Attach scrollbar to listbox
TaskList_list.configure(yscrollcommand=Scrollbar.set)
Scrollbar.configure(command=TaskList_list.yview)
TaskList_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(Prog, text='Add Task', width=12, command=add_task)
add_btn.grid(row=2, column=0, pady=20, padx=10)

remove_btn = Button(Prog, text='Remove Task', width=12, command=remove_task)
remove_btn.grid(row=2, column=1)

clear_btn = Button(Prog, text='Clear Tasks', width=12, command=clear_tasks)
clear_btn.grid(row=2, column=2)
# Populate (Add to textbox list)
populate_list()
# Start program
Prog.mainloop()