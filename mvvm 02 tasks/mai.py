def main():
    from ViewModels.ViewModel import ViewModel
    from Models.listTask import ListTask
    from Views.main import View
    import tkinter as tk
    # Crear el modelo, el ViewModel y la vista
    model = ListTask()
    view_model = ViewModel(model)

    # Crear la ventana de Tkinter
    root = tk.Tk()

    # Crear la vista
    view = View(root, view_model)

    # Iniciar el ciclo principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
