import tkinter as tk
from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path
from tkinter import ttk
from Library.librerias import recoger_sesion, drop_sesion

# Rutas relativas de las imágenes
ASSETS_PATH = Path(r"C:\Pokedex_by_Venezuelan\assets")

# Función para asignar la ruta a las imágenes
def relative_to_assets(path: str) -> Path:
    
    full_path = ASSETS_PATH / Path(path)
    if not full_path.exists():
        raise FileNotFoundError(f"Image not found: {full_path}")
    return full_path

# Clase principal de la aplicación
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("1366x768")
        self.container = tk.Frame(self)
        self.resizable(False, False)  # No permitir cambiar el tamaño de la ventana
        self.container.pack(fill="both", expand=True)
        self.current_frame = None
        self.show_frame(SecondaryPage)

    def show_frame(self, page_class):
        if self.current_frame is not None:
            self.current_frame.pack_forget()
        self.current_frame = page_class(self.container, self)
        self.current_frame.pack(fill="both", expand=True)

class SecondaryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        main_page = Login(self, controller)
        main_page.pack(fill="both", expand=True)

class Login(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}
        canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)

        # Cargar y almacenar las imágenes
        
        self.images["registrar"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        tk.Button(
            self,
            image=self.images["registrar"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame(Registrar),
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)

        # Añadir textos
        canvas.create_text(
            600.0,
            141.0,
            anchor="nw",
            text="Bienvenido",
            fill="#191919",
            font=("Inter", 64 * -1)
        )
        canvas.create_text(
            226.0,
            5.0,
            anchor="nw",
            text="Pokédex",
            fill="#000000",
            font=("Inter", 40 * -1)
        )

        
        canvas.create_text(
            26.0,
            31.0,
            anchor="nw",
            text="Admin",
            fill="#000000",
            font=("Inter", 14 * -1)
        )

class Registrar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}  # Diccionario para almacenar las imágenes

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = tk.Canvas(
            self,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        
        self.images["Bordes"] = tk.PhotoImage(file=relative_to_assets("Bordes.png"))
        self.bordes_image = canvas.create_image(
            683.0,
            389.0,
            image=self.images["Bordes"]
        )

        self.entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            borderwidth=0.5, 
            relief="solid"
        )
        self.entry_1.place(x=507.0, y=349.0, width=352.0, height=38.0)

        self.entry_2 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            borderwidth=0.5, 
            relief="solid"
        )
        self.entry_2.place(x=507.0, y=249.0, width=352.0, height=38.0)
            
        self.entry_3 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            borderwidth=0.5, 
            relief="solid"
        )
        self.entry_3.place(x=507.0, y=449.0, width=352.0, height=38.0)

        canvas.create_text(
            507.0,
            319.0,
            anchor="nw",
            text="Nombre",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            507.0,
            219.0,
            anchor="nw",
            text="Cedula",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            507.0,
            419.0,
            anchor="nw",
            text="Peso",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            627.0,
            163.0,
            anchor="nw",
            text="Registrarse",
            fill="#4C4C4C",
            font=("Montserrat Medium", 20 * -1)
        )
        
        self.button_image_1 = tk.PhotoImage(file=relative_to_assets("L_cancelar.png"))
        self.button_1 = tk.Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: {self.hide_widgets(), self.controller.show_frame(Login)},
            relief="flat"
        )
        self.button_1.place(x=497.0, y=565.0, width=130.0, height=40.0)

        self.button_image_2 = tk.PhotoImage(file=relative_to_assets("L_registrar.png"))
        self.button_2 = tk.Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(x=739.0, y=565.0, width=130.0, height=40.0)

    def hide_widgets(self):
        # Ocultar todos los widgets
        self.entry_1.place_forget()
        self.entry_2.place_forget()
        self.entry_3.place_forget()
        self.button_1.place_forget()
        self.button_2.place_forget()
        canvas = self.winfo_children()[0]
        canvas.itemconfig(self.bordes_image, state='hidden')
            
# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()