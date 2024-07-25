import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
from pathlib import Path
from Vistas.Register import Registrar
from Library.librerias import recoger_sesion,drop_sesion

#Ruta absoluta para las imagenes
ASSETS_PATH = Path(r"C:\Pokedex_by_Venezuelan\assets")

def relative_to_assets(path: str) -> Path:
    full_path = ASSETS_PATH / Path(path)
    if not full_path.exists():
        raise FileNotFoundError(f"Image not found: {full_path}")
    return full_path

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokedex")
        self.geometry("1366x768")
        usuario=recoger_sesion()
        print(usuario)
        self.usuario=usuario
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

class SecondaryPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Crear una instancia de Main_PW como una página dentro de SecondaryPage
        main_page = Main_PW(self, controller)
        main_page.pack(fill="both", expand=True)

class Main_PW(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.usuario=recoger_sesion()
        self.config(bg="#FFFFFF")
        self.create_widgets()
        drop_sesion()

    def create_widgets(self):
        self.images = {}  # Dictionary to store images

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

        # Load and store images
        self.images["image_1"] = tk.PhotoImage(file=relative_to_assets("main_relleno_lateral.png"))
        canvas.create_image(107.0, 412.0, image=self.images["image_1"])

        self.images["image_2"] = tk.PhotoImage(file=relative_to_assets("main_relleno_general.png"))
        canvas.create_image(789.0, 413.0, image=self.images["image_2"])

        self.images["image_3"] = tk.PhotoImage(file=relative_to_assets("main_barra.png"))
        canvas.create_image(682.0, 29.0, image=self.images["image_3"])

        # Store button images
        self.images["button_image_1"] = tk.PhotoImage(file=relative_to_assets("main_boton_volver.png"))
        tk.Button(
            self,
            image=self.images["button_image_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame(Main_PW),
            relief="flat"
        ).place(x=1135.0, y=15.0, width=208.0, height=29.0)
        
        self.images["button_image_5"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        tk.Button(
            self,
            image=self.images["button_image_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.controller.show_frame(Registrar),
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)

        self.images["button_image_2"] = tk.PhotoImage(file=relative_to_assets("main_boton_modificar.png"))
        tk.Button(
            self,
            image=self.images["button_image_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        ).place(x=1.0, y=173.0, width=213.0, height=58.0)

        self.images["button_image_3"] = tk.PhotoImage(file=relative_to_assets("main_boton_listado.png"))
        tk.Button(
            self,
            image=self.images["button_image_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        ).place(x=1.0, y=115.0, width=213.0, height=58.0)

        self.images["button_image_4"] = tk.PhotoImage(file=relative_to_assets("main_boton_eliminar.png"))
        tk.Button(
            self,
            image=self.images["button_image_4"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Eliminar"),
            relief="flat"
        ).place(x=1.0, y=231.0, width=213.0, height=58.0)

        # Add texts
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
            9.0,
            anchor="nw",
            text=self.usuario,
            fill="#000000",
            font=("Inter", 18 * -1)
        )
        canvas.create_text(
            26.0,
            31.0,
            anchor="nw",
            text="Admin",
            fill="#000000",
            font=("Inter", 14 * -1)
        )

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()