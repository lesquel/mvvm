import tkinter as tk
from tkinter import messagebox

class View:
    def __init__(self, master, view_model):
        self.master = master
        self.view_model = view_model

        self.master.title("To-Do List")

        # Lista de tareas
        self.listbox = tk.Listbox(master, height=10, width=50, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Campo para agregar nuevas tareas
        self.title = tk.Entry(master, width=40)
        self.title.pack(pady=10)

         # Campo para agregar nuevas tareas
        self.description = tk.Entry(master, width=40)
        self.description.pack(pady=10)

        # Botón para agregar tarea
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Botón para marcar tarea como completada
        self.toggle_button = tk.Button(master, text="Toggle Completion", command=self.toggle_task)
        self.toggle_button.pack(pady=5)

        self.update_listbox()

    def update_listbox(self):
        """Actualiza la lista de tareas en la vista"""
        self.listbox.delete(0, tk.END)
        for task in self.view_model.get_tasks():
            comple = " completado " if task._completed else " no completado "
            self.listbox.insert(tk.END, task.title + " - " + task.description +  comple)

    def add_task(self):
        from Models.taskDataclass import TaskDataclass
        task = TaskDataclass(self.title.get(), description = self.description.get())
        if task.title and task.description:
            self.view_model.add_task(task)
            self.update_listbox()
            self.title.delete(0, tk.END)
            self.description.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task_to_remove = self.view_model.get_tasks()[selected_task_index]
            self.view_model.remove_task(task_to_remove)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def toggle_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            task_to_toggle = self.view_model.get_tasks()[selected_task_index]
            self.view_model.toggle_task(task_to_toggle)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to toggle completion.")
