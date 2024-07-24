import tkinter as tk
from tkinter import messagebox,ttk
from test import login

def login(user,password):
    Teacher='Oak'
    PassW=5101999
    return Teacher==user and PassW==int(password)

def abrir_ventana():
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("1024x768")
    etiqueta = ttk.Label(nueva_ventana, text="¡Hola desde la nueva ventana!")
    etiqueta.pack()

