import tkinter as tk
from tkinter import ttk
from ViewModels.ContactInformationViewModel import ContactInformationViewModel

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("MVVM Contact App")
        self.viewModel = ContactInformationViewModel()

        # Registrar observadores
        self.viewModel.bind(self.updateView)

        # Crear elementos de la interfaz
        self.createUI()

        # Mostrar datos iniciales
        self.updateView("Constacts")

    def createUI(self):
        # Lista de contactos
        self.contactsList = tk.Listbox(self.root, width=50, height=10)
        self.contactsList.pack(pady=10)

        # Botón para alternar tema
        self.toggleThemeButton = ttk.Button(
            self.root, text="Toggle Theme", command=self.viewModel.toggleDarkMode
        )
        self.toggleThemeButton.pack(pady=10)

    def updateView(self, propertyName: str):
        if propertyName == "Constacts":
            # Actualizar lista de contactos
            self.contactsList.delete(0, tk.END)
            for contact in self.viewModel.Constacts:
                print(contact)
                self.contactsList.insert(tk.END, f"{contact.name} {contact.last_name} - {contact.phone_number} | {contact.gender}")
            return

        elif propertyName == "isDarkMode":
            # Actualizar tema de la interfaz
            if self.viewModel.isDarkMode:
                self.root.config(bg="black")
                self.contactsList.config(bg="gray", fg="white")
            else:
                self.root.config(bg="white")
                self.contactsList.config(bg="white", fg="black")

            return
