"""import sys
sys.path.append("..") 
"""
from pathlib import Path

from Main_F.Main_PWindow import *

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"E:\Documentos mios XD\tkDesigner\Pokedex\Pokedex_app\Selection\assets\frame0")
           
class selection():
    def open(self):
        
        
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        window = Tk()

        window.geometry("1366x768")
        window.configure(bg = "#FFFFFF")

        Main_PW=Main_PW()

        canvas = Canvas(
            window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            557.0,
            79.0,
            anchor="nw",
            text="Seleccione",
            fill="#000000",
            font=("Montserrat Regular", 48 * -1)
        )

        canvas.create_text(
            540.0,
            118.0,
            anchor="nw",
            text="el área a gestionar",
            fill="#000000",
            font=("Montserrat Regular", 32 * -1)
        )
        #boton1= Pokemones
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            280.0,
            459.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: Main_PW.open(),
            relief="flat"
        )
        button_1.place(
            x=245.0,
            y=260.0,
            width=130.0,
            height=40.0
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(
            1057.0,
            469.0,
            image=image_image_2
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=991.0,
            y=260.0,
            width=130.0,
            height=40.0
        )
        window.resizable(False, False)
        window.mainloop()

selection=selection()
selection.open()