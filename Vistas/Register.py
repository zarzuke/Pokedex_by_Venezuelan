import tkinter as tk
from pathlib import Path
from tkinter import ttk

# Rutas relativas de las imágenes
ASSETS_PATH = Path(r"C:\Pokedex_by_Venezuelan\assets")

# Función para asignar la ruta a las imágenes
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
        self.images["button_image_5"] = tk.PhotoImage(file=relative_to_assets("main_boton_registrar.png"))
        tk.Button(
            self,
            image=self.images["button_image_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        ).place(x=1.0, y=57.0, width=213.0, height=58.0)
        
        self.images["button_image_1"] = tk.PhotoImage(file=relative_to_assets("main_boton_volver.png"))
        tk.Button(
            self,
            image=self.images["button_image_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: None,
            relief="flat"
        ).place(x=1135.0, y=15.0, width=208.0, height=29.0)

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
            command=lambda: print("Boton eliminar"),
            relief="flat"
        ).place(x=1.0, y=231.0, width=213.0, height=58.0)
        
        #Formulario para el registro
        
        # Titulos de los inputs
        canvas.create_text(263.0, 106.0, anchor="nw", text="Ingrese la información del pokemon a agregar", fill="#4C4C4C", font=("Montserrat Medium", 15))
        canvas.create_text(805.0, 152.0, anchor="nw", text="Subir imagen pokemon", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 152.0, anchor="nw", text="Nombre", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(520.0, 149.0, anchor="nw", text="Tipo", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 252.0, anchor="nw", text="Peso", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(520.0, 252.0, anchor="nw", text="Altura", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(779.0, 253.0, anchor="nw", text="Sexo", fill="#000000", font=("Montserrat Regular", 15))
        canvas.create_text(263.0, 352.0, anchor="nw", text="Descripción", fill="#000000", font=("Montserrat Regular", 15))
        #-------------------------------------------------------------------------------------
        # Crear y colocar los widgets
        nombre = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=520.0, y=282.0, width=237.0, height=38.0)

        peso = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=263.0, y=182.0, width=237.0, height=38.0)

        altura = tk.Entry(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, borderwidth=0.5, relief="solid").place(x=263.0, y=282.0, width=237.0, height=37.5)
        
        #Select tipo de pokemon
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",
                        fieldbackground="#FFFFFF",  # Fondo del campo de entrada
                        background="#FF0000",  # Fondo del desplegable
                        bordercolor="#000716",  # Color del borde
                        arrowcolor="#FFFFFF",  # Color de la flecha
                        padding= "9",
                        ) # padding para agrandar la altura del select
        
        pokemon_types = [
        "Agua", "Bicho", "Dragón", "Eléctrico", "Fuego", "Hada", "Hielo",
        "Lucha", "Normal", "Planta", "Psíquico", "Roca", "Siniestro", "Tierra",
        "Veneno", "Volador"
        ]
        
        tipos_de_pokemones = ttk.Combobox(self, values=pokemon_types, state="readonly", width=30, font=("Montserrat Medium", 10)).place(x=520.0, y=181.5)
        #-------------------------------------------------------------------------------
        # Select sexo del pokemon
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox",
                        fieldbackground="#FFFFFF",  # Fondo del campo de entrada
                        background="#FF0000",  # Fondo del desplegable
                        bordercolor="#000716",  # Color del borde
                        arrowcolor="#FFFFFF",  # Color de la flecha
                        padding= "9",
                        ) # padding para agrandar la altura del select
        
        pokemon_sex = ["Masculino", "Femenino"]
        
        tipos_de_sexo = ttk.Combobox(self, values=pokemon_sex, state="readonly", width=30, font=("Montserrat Medium", 10)).place(x=779.0, y=282.0)
        #-------------------------------------------------------------------------------
        # TextArea
        text_area = tk.Text(self, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, wrap=tk.WORD)
        text_area.place(x=265.0, y=382.0, width=751.0, height=238.0)
        
        # Ajustar la apariencia del Text widget para que se parezca al Entry
        text_area.config(font=("Montserrat Medium", 10), padx=10, pady=10, borderwidth=0.5, relief="solid")
        #-------------------------------------------------------------------------------
        # Cargar y almacenar las imágenes
        self.images['boton_R'] = tk.PhotoImage(file=relative_to_assets("R_Boton_registrar.png"))
        self.images['pokebola_off'] = tk.PhotoImage(file=relative_to_assets("R_Pokebola_off.png"))
        self.images['pokebola_on'] = tk.PhotoImage(file=relative_to_assets("R_Pokebola_on.png"))
        
         # Inicializar la variable booleana
        self.change_pokeball = False
        
        # Crear el botón con la imagen inicial
        self.button = tk.Button(
            self,
            image=self.images["pokebola_off"],
            background="#ffffff",        # Fondo del botón
            activebackground="#ffffff",  # Fondo del botón cuando está activo
            relief="flat",               # Sin relieve en el botón
            bd=0,                        # Sin borde en el botón
            command=lambda:activar_otra_pokebola(self)
        )
        self.button.place(x=870.0, y=177.0)

        #Funcion para activar el color de la pokebola
        def activar_otra_pokebola(self):
            # Cambiar el estado de la variable booleana
            self.change_pokeball = not self.change_pokeball
        
            # Actualizar la imagen del botón según el estado de la variable
            if self.change_pokeball:
                self.button.config(image=self.images["pokebola_on"])
            else:
                self.button.config(image=self.images["pokebola_off"])

        # Crear el botón
        boton_R = self.images['boton_R']
        tk.Button(
            self,
            image=boton_R,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("B_registrar clicked"),
            relief="flat",
        ).place(x=265.0, y=635.0, width=130.0, height=40.0)
        
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