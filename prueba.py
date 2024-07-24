import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación con Contenido Dinámico")
        self.geometry("400x300")

        # Crear un contenedor para las diferentes vistas
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Crear y mostrar la vista inicial
        self.current_frame = None
        self.show_frame(HomePage)

    def show_frame(self, page_class):
        # Ocultar la vista actual si existe
        if self.current_frame is not None:
            self.current_frame.pack_forget()

        # Crear una nueva vista y mostrarla
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

        # Etiqueta en la página secundaria
        label = tk.Label(self, text="Página Secundaria")
        label.pack(pady=20)

        # Botón para volver a la página principal
        change_page_button = tk.Button(self, text="Volver a la Página Principal",
                                       command=lambda: controller.show_frame(HomePage))
        change_page_button.pack(pady=10)

# Crear y ejecutar la aplicación
app = App()
app.mainloop()
