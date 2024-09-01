import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):  
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.pack(pady=5)

        self.entry_frame = tk.Frame(self.frame)
        self.entry_frame.pack(pady=5)

        self.task_entry = tk.Entry(self.entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "The task cannot be empty.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index[0])
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":  
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()