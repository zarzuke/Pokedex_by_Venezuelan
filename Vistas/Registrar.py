import tkinter as tk
from pathlib import Path
from Registrar import *
# Rutas relativa de las imagenes
ASSETS_PATH = Path(r"C:\Pokedex_by_Venezuelan\assets")

# Funcion para asignar la ruta a las imagenes
def relative_to_assets(path: str) -> Path:
    full_path = ASSETS_PATH / Path(path)
    if not full_path.exists():
        raise FileNotFoundError(f"Image not found: {full_path}")
    return full_path

class Registrar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.config(bg="#FFFFFF")
        self.create_widgets()

    def create_widgets(self):
        self.images = {}

    canvas = tk.Canvas(
        Registrar,
        bg="#FFFFFF",
        height=768,
        width=1366,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)

    def show_Registrar():
        button_image_1 = tk.PhotoImage(
            file=relative_to_assets("R_Boton_registrar.png"))
        button_1 = tk.Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("B_registrar clicked"),
            relief="flat"
        )
        button_1.place(
            x=265.0,
            y=680.0,
            width=130.0,
            height=40.0
        )

        entry_image_1 = tk.PhotoImage(
            file=relative_to_assets("R_entry_1.png"))
        entry_bg_1 = canvas.create_image(
            638.5,
            302.0,
            image=entry_image_1
        )
        entry_1 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_1.place(
            x=520.0,
            y=282.0,
            width=237.0,
            height=38.0
        )

        entry_image_2 = tk.PhotoImage(
            file=relative_to_assets("R_entry_2.png"))
        entry_bg_2 = canvas.create_image(
            381.5,
            202.0,
            image=entry_image_2
        )
        entry_2 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_2.place(
            x=263.0,
            y=182.0,
            width=237.0,
            height=38.0
        )

        entry_image_3 = tk.PhotoImage(
            file=relative_to_assets("R_entry_3.png"))
        entry_bg_3 = canvas.create_image(
            381.5,
            302.0,
            image=entry_image_3
        )
        entry_3 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_3.place(
            x=263.0,
            y=282.0,
            width=237.0,
            height=38.0
        )

        entry_image_4 = tk.PhotoImage(
            file=relative_to_assets("R_entry_4.png"))
        entry_bg_4 = canvas.create_image(
            640.5,
            502.0,
            image=entry_image_4
        )
        entry_4 = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        entry_4.place(
            x=265.0,
            y=382.0,
            width=751.0,
            height=238.0
        )

        canvas.create_text(
            520.0,
            252.0,
            anchor="nw",
            text="Altura",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            263.0,
            152.0,
            anchor="nw",
            text="Nombre",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            263.0,
            352.0,
            anchor="nw",
            text="Descripcion",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            263.0,
            252.0,
            anchor="nw",
            text="Peso",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            520.0,
            149.0,
            anchor="nw",
            text="Tipo",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        image_image_1 = tk.PhotoImage(
            file=relative_to_assets("R_PH_M1.png"))
        image_1 = canvas.create_image(
            638.0,
            199.0,
            image=image_image_1
        )

        image_image_2 = tk.PhotoImage(
            file=relative_to_assets("R_PH_F1.png"))
        image_2 = canvas.create_image(
            746.9999997774548,
            190.99999904632568,
            image=image_image_2
        )

        canvas.create_text(
            530.0,
            187.0,
            anchor="nw",
            text="Fuego",
            fill="#4C4C4C",
            font=("Montserrat Regular", 15 * -1)
        )

        image_image_3 = tk.PhotoImage(
            file=relative_to_assets("R_PH_M2.png"))
        image_3 = canvas.create_image(
            897.0,
            297.0,
            image=image_image_3
        )

        image_image_4 = tk.PhotoImage(
            file=relative_to_assets("R_PH_F2.png"))
        image_4 = canvas.create_image(
            1005.9999997774548,
            288.9999990463257,
            image=image_image_4
        )

        canvas.create_text(
            789.0,
            285.0,
            anchor="nw",
            text="Femenino",
            fill="#4C4C4C",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            779.0,
            247.0,
            anchor="nw",
            text="Sexo",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        canvas.create_text(
            263.0,
            106.0,
            anchor="nw",
            text="Añada la información del pokemon a agregar",
            fill="#4C4C4C",
            font=("Montserrat Medium", 15 * -1)
        )

        canvas.create_text(
            805.0,
            152.0,
            anchor="nw",
            text="Subir imagen pokemon",
            fill="#000000",
            font=("Montserrat Regular", 15 * -1)
        )

        image_image_5 = tk.PhotoImage(
            file=relative_to_assets("R_Pokebola_off.png"))
        image_5 = canvas.create_image(
            890.0,
            212.0,
            image=image_image_5
        )

        image_image_6 = tk.PhotoImage(
            file=relative_to_assets("R_Pokebola_on.png"))
        image_6 = canvas.create_image(
            1213.0,
            212.0,
            image=image_image_6
        )