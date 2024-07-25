import tkinter as tk
from tkinter import ttk

def create_pokemon_combobox(root):
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",
                    fieldbackground="#FFFFFF",  # Fondo del campo de entrada
                    background="#FF0000",  # Fondo del desplegable
                    bordercolor="#FF0000",  # Color del borde
                    arrowcolor="#FFFFFF",  # Color de la flecha
                    font=('Helvetica', 12))  # Fuente y tamaño de texto
    
    pokemon_types = [
    "Agua", "Bicho", "Dragón", "Eléctrico", "Fuego", "Hada", "Hielo",
    "Lucha", "Normal", "Planta", "Psíquico", "Roca", "Siniestro", "Tierra",
    "Veneno", "Volador"
    ]
    
    combobox = ttk.Combobox(root, values=pokemon_types, state="readonly", width=20)
    combobox.set("Selecciona un tipo")
    combobox.pack(pady=20)
    
    return combobox

root = tk.Tk()
root.title("Pokémon Combobox")
root.geometry("300x200")

combobox = create_pokemon_combobox(root)

root.mainloop()
