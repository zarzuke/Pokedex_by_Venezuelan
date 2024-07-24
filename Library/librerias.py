import tkinter as tk
from tkinter import messagebox,ttk
from test import login
import sqlite3

def login(user,password):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("SELECT usuarioPsw FROM usuarios WHERE usuarioNombre = ?" , (user,))
    pw=cursor.fetchone()
    return pw and pw[0]== password

def abrir_ventana():
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("1024x768")
    etiqueta = ttk.Label(nueva_ventana, text="¡Hola desde la nueva ventana!")
    etiqueta.pack()

