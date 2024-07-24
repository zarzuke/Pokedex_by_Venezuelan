import sqlite3
import tkinter as tk
from PIL import Image, ImageTk
import io

conn = sqlite3.connect('imagenes.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS imagenes
             (id INTEGER PRIMARY KEY, nombre TEXT, imagen BLOB)''')
conn.commit()
conn.close()

def convertir_a_binario(ruta_imagen):
    with open(ruta_imagen, 'rb') as file:
        blob_data = file.read()
    return blob_data

def guardar_imagen(nombre, ruta_imagen):
    conn = sqlite3.connect('imagenes.db')
    c = conn.cursor()
    imagen_binaria = convertir_a_binario(ruta_imagen)
    c.execute("INSERT INTO imagenes (nombre, imagen) VALUES (?, ?)", (nombre, imagen_binaria))
    conn.commit()
    conn.close()

# Ejemplo de uso
guardar_imagen('ejemplo', 'ruta/a/tu/imagen.jpg')

def recuperar_imagen(nombre):
    conn = sqlite3.connect('imagenes.db')
    c = conn.cursor()
    c.execute("SELECT imagen FROM imagenes WHERE nombre=?", (nombre,))
    imagen_binaria = c.fetchone()[0]
    conn.close()
    return imagen_binaria

def mostrar_imagen(nombre):
    imagen_binaria = recuperar_imagen(nombre)
    imagen = Image.open(io.BytesIO(imagen_binaria))
    render = ImageTk.PhotoImage(imagen)

    ventana = tk.Tk()
    etiqueta = tk.Label(ventana, image=render)
    etiqueta.image = render
    etiqueta.pack()
    ventana.mainloop()

# Ejemplo de uso
mostrar_imagen('ejemplo')
