import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x500")
root.config(bg="#a4bed2")

tasks = []

def add_task():
    task = task_entry.get()

    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = tasks[selected_task_index]

        if not task.startswith("✔ "):
            tasks[selected_task_index] = "✔ " + task

        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def update_listbox():
    task_listbox.delete(0, tk.END)

    for task in tasks:
        task_listbox.insert(tk.END, task)

title_label = tk.Label(
    root,
    text="To-Do List Application",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="blue"
)
title_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Arial", 12),
    width=12,
    command=add_task
)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    font=("Arial", 12),
    width=12,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)

complete_button = tk.Button(
    button_frame,
    text="Mark Complete",
    font=("Arial", 12),
    width=15,
    command=mark_completed
)
complete_button.grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=40,
    height=15,
    selectbackground="lightblue"
)
task_listbox.pack(pady=20)

root.mainloop()
