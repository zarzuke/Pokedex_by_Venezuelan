from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pokedex_by_Venezuelan\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class M_Usuarios():
    def open():
        window = Tk()

        window.geometry("1366x768")
        window.configure(bg = "#FFFFFF")


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
        image_image_1 = PhotoImage(
            file=relative_to_assets("U_relleno_vertical.png"))
        image_1 = canvas.create_image(
            107.0,
            412.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("U_relleno_general.png"))
        image_2 = canvas.create_image(
            789.0,
            413.0,
            image=image_image_2
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("U_barra.png"))
        image_3 = canvas.create_image(
            682.0,
            29.0,
            image=image_image_3
        )

        canvas.create_text(
            600.0,
            141.0,
            anchor="nw",
            text="Bienvenido",
            fill="#191919",
            font=("Inter", 64 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("U_volver.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="raised",
            bg="#6D6CFA",
            activebackground="#6D6CFA"
        )
        button_1.place(
            x=1135.0,
            y=15.0,
            width=208.0,
            height=29.0
        )

        canvas.create_text(
            226.0,
            5.0,
            anchor="nw",
            text="Gestion de Usuarios",
            fill="#000000",
            font=("Inter", 40 * -1)
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("U_modificar.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=1.0,
            y=57.0,
            width=213.0,
            height=58.0

        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("U_listado.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=1.0,
            y=173.0,
            width=213.0,
            height=58.0
            
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("U_eliminar.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=1.0,
            y=115.0,
            width=213.0,
            height=58.0
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
        window.resizable(False, False)
        window.mainloop()
        
#M_Usuarios.open()