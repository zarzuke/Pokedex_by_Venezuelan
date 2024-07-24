import tkinter as tk
from tkinter import messagebox,ttk
from test import login

def recoger_datos():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    if login(usuario, contrasena):
        messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
        root.destroy()
        abrir_ventana()

    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def abrir_ventana():
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("1024x768")
    etiqueta = ttk.Label(nueva_ventana, text="¡Hola desde la nueva ventana!")
    etiqueta.pack()


root = tk.Tk()
root.title("Login")
root.geometry("1024x768")
label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_contrasena = tk.Label(root, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = tk.Entry(root, show="*")  # Muestra asteriscos en lugar de la contraseña
entry_contrasena.pack()

boton_login = tk.Button(root, text="Iniciar sesión", command=recoger_datos)
boton_login.pack()

root.mainloop()

#hola

