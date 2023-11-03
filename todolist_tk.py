import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Пустая задача", "Пожалуйста, введите текст задачи.")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def edit_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        new_task = task_entry.get()
        if new_task:
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Пустая задача", "Пожалуйста, введите задачу.")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


root = tk.Tk()
root.title("Список задач")


task_entry = tk.Entry(root)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Добавить задачу", command=add_task).pack()
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task).pack()
edit_button = tk.Button(root, text="Редактировать задачу", command=edit_task).pack()
save_button = tk.Button(root, text="Сохранить задачи", command=save_tasks).pack()
task_listbox = tk.Listbox(root)
task_listbox.pack()

root.mainloop()
