from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Button, PhotoImage

#Rutas relativas para las imagenes
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pokedex_by_Venezuelan\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Clase principal de la aplicación
class Users(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokedex")
        self.geometry("1366x768")
        self.resizable(False, False)  # No permitir cambiar el tamaño de la ventana
        self.container = tk.Frame(self)
        self.iconbitmap(relative_to_assets('PokeBall.ico'))
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
        main_page = M_Usuarios(self, controller)
        main_page.pack(fill="both", expand=True)

class M_Usuarios(tk.Frame):
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
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("U_relleno_vertical.png"))
        canvas.create_image(
            107.0,
            412.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("U_relleno_general.png"))
        canvas.create_image(
            789.0,
            413.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("U_barra.png"))
        canvas.create_image(
            682.0,
            29.0,
            image=self.image_image_3
        )
        
        #Texto del navbar
        canvas.create_text(
            26.0,
            9.0,
            anchor="nw",
            text="Cesar Maldonado",
            fill="#000000",
            font=("Inter", 18 * -1)
        )

        #Texto del navbar
        canvas.create_text(
            26.0,
            31.0,
            anchor="nw",
            text="Admin",
            fill="#000000",
            font=("Inter", 14 * -1)
        )
        
        #Texto del navbar
        canvas.create_text(
            600.0,
            141.0,
            anchor="nw",
            text="Bienvenido",
            fill="#191919",
            font=("Inter", 64 * -1)
        )
        
        #Texto del navbar
        canvas.create_text(
            226.0,
            5.0,
            anchor="nw",
            text="Gestion de Usuarios",
            fill="#000000",
            font=("Inter", 40 * -1)
        )

        #Boton para regresar a la seleccion
        self.images["button_volver"] = tk.PhotoImage(file=relative_to_assets("U_volver.png"))
        tk.Button(
            image=self.images["button_volver"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="raised",
            bg="#6D6CFA",
            activebackground="#6D6CFA"
        ).place(x=1135.0, y=15.0, width=208.0, height=29.0)
        
        #Boton listar para ver a los usuarios
        self.images["button_listado"] = tk.PhotoImage(file=relative_to_assets("U_listado.png"))
        tk.Button(
            self,
            image=self.images["button_listado"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)
        
        #Boton para modicar el usuario
        self.images["button_modificar"] = tk.PhotoImage(file=relative_to_assets("U_modificar.png"))
        tk.Button(
            self,
            image=self.images["button_modificar"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        ).place(x=1.0,y=115.0,width=213.0,height=58.0)
        
        #Boton para enviar a la accion de eliminar al usuario
        self.images["button_eliminar"] = tk.PhotoImage(file=relative_to_assets("U_modificar.png"))
        tk.Button(
            self,
            image=self.images["button_eliminar"],
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        ).place(x=1.0, y=173.0, width=213.0, height=58.0)

class Eliminar():
    pass
# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = Users()
    app.mainloop()