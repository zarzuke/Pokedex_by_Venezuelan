from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Pokedex_by_Venezuelan\assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
button_image_1 = PhotoImage(
    file=relative_to_assets("Boton_eliminar.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=265.0,
    y=264.0,
    width=130.0,
    height=40.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("R_entry_1.png"))
entry_bg_1 = canvas.create_image(
    381.5,
    202.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=263.0,
    y=182.0,
    width=237.0,
    height=38.0
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
    266.0,
    106.0,
    anchor="nw",
    text="Añada la información del pokemon a Eliminar",
    fill="#4C4C4C",
    font=("Montserrat Medium", 15 * -1)
)
window.resizable(False, False)
window.mainloop()