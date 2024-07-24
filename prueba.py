import tkinter as tk
from tkinter import messagebox, ttk
from Vistas.Main_PWindow import Main_PW

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokedex")
        self.geometry("1366x768")

        # Contenedor para las diferentes vistas
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Mostrar la vista inicial
        self.current_frame = None
        self.show_frame(SecondaryPage)

    def show_frame(self, page_class):
        # Oculta la vista actual si existe
        if self.current_frame is not None:
            self.current_frame.pack_forget()

        # Crea una nueva vista y la muestra
        self.current_frame = page_class(self.container, self)
        self.current_frame.pack(fill="both", expand=True)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Etiqueta en la página principal
        label = tk.Label(self, text="Página Principal")
        label.pack(pady=20)

        # Botón para cambiar a la página secundaria
        change_page_button = tk.Button(self, text="Ir a la Página Secundaria",
                                       command=lambda: controller.show_frame(SecondaryPage))
        change_page_button.pack(pady=10)

class SecondaryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Crear una instancia de Main_PW como una página dentro de SecondaryPage
        main_page = Main_PW(self, controller)
        main_page.pack(fill="both", expand=True)

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()
