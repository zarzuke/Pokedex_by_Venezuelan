import tkinter as tk
from Main_PWindow import *
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configuración de la apariencia de la página principal
        self.configure(bg="#FFFFFF")
        self.pack(fill="both", expand=True)  # Asegura que el frame ocupe todo el espacio del contenedor

        # Etiqueta de bienvenida
        label = tk.Label(self, text="Bienvenido a la Página Principal", font=("Arial", 18))
        label.pack(pady=20)

        # Botones u otros widgets que puedas necesitar
        button1 = tk.Button(self, text="Ir a otra página",
                            command=lambda: controller.show_frame(OtraPagina))
        button1.pack()

        button2 = tk.Button(self, text="Hacer algo más",
                            command=lambda: self.hacer_algo())
        button2.pack()

    def hacer_algo(self):
        main=Main_PW()
        main.open()
        print("Se hizo algo desde la página principal")

# Ejemplo de cómo usar la clase HomePage en una aplicación
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mi Aplicación")
        self.geometry("600x400")

        # Contenedor para las diferentes vistas
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Mostrar la página principal al inicio
        self.show_frame(HomePage)

    def show_frame(self, page_class):
        # Ocultar la vista actual si existe
        if self.container.winfo_children():
            self.container.winfo_children()[0].pack_forget()

        # Crear una nueva vista y mostrarla
        page = page_class(self.container, self)
        page.pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
