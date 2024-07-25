import tkinter as tk
from pathlib import Path

# Rutas relativa de las imagenes
ASSETS_PATH = Path(r"C:\Pokedex_by_Venezuelan\assets")

# Funcion para asignar la ruta a las imagenes
def relative_to_assets(path: str) -> Path:
    full_path = ASSETS_PATH / Path(path)
    if not full_path.exists():
        raise FileNotFoundError(f"Image not found: {full_path}")
    return full_path

#La clase App Actúa como la ventana principal de la aplicación. Maneja la creación y el cambio de diferentes vistas dentro de la aplicación.
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pokedex")
        self.geometry("1366x768")
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        
        # Mostrar la vista inicial
        self.current_frame = None
        self.show_frame(Main_PW)

    def show_frame(self, page_class):
        if self.current_frame is not None:
            self.current_frame.destroy()  # Mejor uso de destroy para liberar recursos

        self.current_frame = page_class(self.container, self)
        self.current_frame.pack(fill="both", expand=True)

class Main_PW(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}
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

        # Cargar y almacenar las imágenes
        self.images["image_1"] = tk.PhotoImage(file=relative_to_assets("main_relleno_lateral.png"))
        canvas.create_image(107.0, 412.0, image=self.images["image_1"])

        self.images["image_2"] = tk.PhotoImage(file=relative_to_assets("main_relleno_general.png"))
        canvas.create_image(789.0, 413.0, image=self.images["image_2"])

        self.images["image_3"] = tk.PhotoImage(file=relative_to_assets("main_barra.png"))
        canvas.create_image(682.0, 29.0, image=self.images["image_3"])

        # Botón para regresar al estado "Bienvenido"
        self.images["button_image_1"] = tk.PhotoImage(file=relative_to_assets("main_boton_volver.png"))
        tk.Button(
            self,
            image=self.images["button_image_1"],
            borderwidth=0,
            highlightthickness=0,
            command=self.show_welcome,
            relief="flat"
        ).place(x=1135.0, y=15.0, width=208.0, height=29.0)

        # Botones para cada acción
        self.images["button_image_2"] = tk.PhotoImage(file=relative_to_assets("main_boton_modificar.png"))
        tk.Button(
            self,
            image=self.images["button_image_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_action("Modificar"),
            relief="flat"
        ).place(x=1.0, y=173.0, width=213.0, height=58.0)

        self.images["button_image_3"] = tk.PhotoImage(file=relative_to_assets("main_boton_listado.png"))
        tk.Button(
            self,
            image=self.images["button_image_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_action("Listado"),
            relief="flat"
        ).place(x=1.0, y=115.0, width=213.0, height=58.0)

        self.images["button_image_4"] = tk.PhotoImage(file=relative_to_assets("main_boton_eliminar.png"))
        tk.Button(
            self,
            image=self.images["button_image_4"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_action("Eliminar"),
            relief="flat"
        ).place(x=1.0, y=231.0, width=213.0, height=58.0)

        self.images["button_image_5"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        tk.Button(
            self,
            image=self.images["button_image_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_action("Registrar"),
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)

        # Añadir textos iniciales
        self.text_id = canvas.create_text(
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
            text="Cesar Maldonado",
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

        self.canvas = canvas

    #Metodo que gestiona las diferentes acciones y llamados de otros metodos dependiendo de su necesidad
    def show_action(self, action):
        # Oculta los widgets anteriores
        self.hide_widgets()

        # Actualiza el texto según la acción y muestra los widgets necesarios
        self.canvas.itemconfig(self.text_id, text=action)

        # Llama a la función específica para mostrar la entrada y el botón
        if action == "Eliminar":
            self.show_entry("Eliminar")
        elif action == "Registrar":
            self.show_entry("Registrar")
        elif action == "Modificar":
            self.show_entry("Modificar")
        elif action == "Listado":
            pass

    def show_entry(self, action):
        # Muestra un Entry y un botón para confirmar la acción
        self.entry = tk.Entry(self, font=("Inter", 24))
        self.entry.place(x=600, y=200, width=300, height=40)
        self.entry.focus_set()

        # Botón para confirmar la acción
        self.action_button = tk.Button(
            self,
            text="Confirmar",
            command=lambda: self.confirm_action(action),
            font=("Inter", 18)
        )
        self.action_button.place(x=600, y=250, width=100, height=30)

    def confirm_action(self, action):
        # Aquí puedes agregar la lógica para manejar cada acción
        self.hide_widgets()
        self.canvas.itemconfig(self.text_id, text=f"{action} Confirmado")  # Cambia el texto de vuelta

    def show_welcome(self):
        # Regresa al estado "Bienvenido"
        self.hide_widgets()
        self.canvas.itemconfig(self.text_id, text="Bienvenido")

    def hide_widgets(self):
        # Oculta los widgets que no sean necesarios en el estado actual
        if hasattr(self, 'entry'):
            self.entry.place_forget()
        if hasattr(self, 'action_button'):
            self.action_button.place_forget()

# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app = App()
    app.mainloop()