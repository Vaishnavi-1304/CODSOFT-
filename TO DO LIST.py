import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("500x550")
        self.root.config(bg="#f0f0f0")  # Light grey background
        
        # Customizing the font
        self.font = ('Arial', 12)
        
        # Task entry
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.root, textvariable=self.task_var, font=self.font, bd=2)
        self.task_entry.pack(pady=20)
        
        # Add task button
        self.add_task_btn = tk.Button(self.root, text="Add Task", command=self.add_task, font=self.font, bg="#cfcfcf", fg="black")
        self.add_task_btn.pack(pady=5)
        
        # Listbox to display tasks with scrollbar
        self.list_frame = tk.Frame(self.root)
        self.list_frame.pack(pady=20)
        
        self.list_scroll = tk.Scrollbar(self.list_frame)
        self.list_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.tasks_listbox = tk.Listbox(self.list_frame, width=50, height=15, font=self.font, bg="white", bd=0, yscrollcommand=self.list_scroll.set)
        self.tasks_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        
        self.list_scroll.config(command=self.tasks_listbox.yview)
        
        # Delete selected task button
        self.del_task_btn = tk.Button(self.root, text="Delete Selected Task", command=self.delete_task, font=self.font, bg="#cfcfcf", fg="black")
        self.del_task_btn.pack(pady=5)

        # Delete all tasks button
        self.del_all_tasks_btn = tk.Button(self.root, text="Delete All Tasks", command=self.delete_all_tasks, font=self.font, bg="#cfcfcf", fg="black")
        self.del_all_tasks_btn.pack(pady=5)
        
        # Placeholder for tasks (later can be replaced with database or file)
        self.tasks = []

    def add_task(self):
        task = self.task_var.get()
        if task != "":
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.task_var.set("")  # Clear the entry box
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_tasks_listbox(self):
        self.tasks_listbox.delete(0, tk.END)  # Clear current list
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)
    
    def delete_task(self):
        try:
            # Get selected task index and remove it from the list
            selected_task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")
    
    def delete_all_tasks(self):
        response = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
        if response:
            self.tasks.clear()  # Clear the tasks list
            self.update_tasks_listbox()  # Update the listbox to reflect the empty tasks list

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()