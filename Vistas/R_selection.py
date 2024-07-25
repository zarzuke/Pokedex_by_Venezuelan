from pathlib import Path

from Vistas.Main_PWindow import *
from Vistas.U_main import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pokedex_by_Venezuelan\assets")
           
class selection():
    def open_new(self):
        self.window.destroy()
        App().show_frame()
        
    def open_U_main(self):
        self.window.destroy()
        M_Usuarios.open()
        
    def open(self):
        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        self.window = Tk()

        self.window.geometry("1366x768")
        self.window.configure(bg = "#FFFFFF")
        #Configuramos el icono de la aplicación
        self.window.iconbitmap(relative_to_assets('PokeBall.ico'))

        #Main_PW=Main_PW()

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_text(
            210.0,
            79.0,
            anchor="nw",
            text="Seleccione el área a gestionar",
            fill="#000000",
            font=("Press Start 2P", 32 * -1)
        )

        #boton1= Pokemones
        image_image_1 = PhotoImage(
            file=relative_to_assets("charmander.png"))
        canvas.create_image(
            280.0,
            459.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_pokemones.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_new(),
            relief="flat"
        )
        button_1.place(
            x=245.0,
            y=230.0,
            width=130.0,
            height=40.0
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("entrenador.png"))
        resized_image = image_image_2.subsample(4,4)
        canvas.create_image(
            1057.0,
            469.0,
            image=resized_image
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_usuarios.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_U_main(),
            relief="flat"
        )
        button_2.place(
            x=991.0,
            y=230.0,
            width=130.0,
            height=40.0
        )
        
        self.window.resizable(False, False)
        self.window.mainloop()

""" selection=selection()
selection.open() """