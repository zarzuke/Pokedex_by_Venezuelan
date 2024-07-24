import tkinter as tk
from tkinter import ttk

def abrir_ventana():
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("300x200")
    etiqueta = ttk.Label(nueva_ventana, text="¡Hola desde la nueva ventana!")
    etiqueta.pack()

root = tk.Tk()
root.title("Botón en Tkinter")
root.geometry("300x200")

boton = ttk.Button(root, text="Abrir Nueva Ventana", command=abrir_ventana)
boton.place(x=50, y=50)

root.mainloop()
