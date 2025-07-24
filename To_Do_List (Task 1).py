import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

root = tk.Tk()
root.title("To-Do List")

tasks = []

tk.Label(root,text="Task").grid(row=0,column=0,padx=5,pady=5,sticky="w")
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0,column=1,padx=5,pady=5,columnspan=2)

tk.Label(root,text="Due Date").grid(row=1,column=0,padx=5,pady=5,sticky="w")
due_date=DateEntry(root,date_pattern='dd-mm-yyyy')
due_date.grid(row=1,column=1,padx=5,pady=5)

tk.Label(root,text="Priority").grid(row=1,column=2,padx=5,pady=5,sticky="w")
priority_var=tk.StringVar(value="Low")
priority_menu=ttk.Combobox(root,textvariable=priority_var,values=["High","Medium","Low"],state="readonly")
priority_menu.grid(row=1, column=3, padx=5, pady=5)

task_frame = tk.Frame(root)
task_frame.grid(row=4,column=0,columnspan=4,padx=10,pady=10,sticky="nsew")
canvas = tk.Canvas(task_frame, height=200)
scrollbar = ttk.Scrollbar(task_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

def toggle_task(task):
    label = task["label"]
    if task["var"].get():
        label.config(fg="grey",font=("Arial",10,"overstrike"))
    else:
        label.config(fg="black",font=("Arial",10,"normal"))

def refresh_tasks():
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    task_list=tasks.copy()
    if sort_by_priority.get():
        priority_order={"High":1,"Medium":2,"Low":3}
        task_list.sort(key=lambda x:priority_order.get(x["priority"], 4))
    for task in task_list:
        frame=tk.Frame(scrollable_frame)
        frame.pack(anchor="w",fill="x",pady=2)
        cb=tk.Checkbutton(frame,variable=task["var"],command=lambda t=task:toggle_task(t))
        cb.pack(side="left")
        label = tk.Label(frame,text=f'{task["text"]} (Due: {task["date"]}) [Priority: {task["priority"]}]',anchor="w")
        label.pack(side="left")
        task["label"] = label

def add_task():
    text=task_entry.get().strip()
    date=due_date.get_date()
    priority=priority_var.get()
    if not text:
        return
    var=tk.BooleanVar()
    task={"text": text,"date":date,"priority":priority,"var":var,"label":None}
    tasks.append(task)
    task_entry.delete(0, tk.END)
    refresh_tasks()

add_button=tk.Button(root,text="Add Task",command=add_task)
add_button.grid(row=2,column=1,pady=10)
sort_by_priority = tk.BooleanVar()
sort_cb = tk.Checkbutton(root,text="Sort by Priority",variable=sort_by_priority,command=refresh_tasks)
sort_cb.grid(row=3, column=1)
root.mainloop()
