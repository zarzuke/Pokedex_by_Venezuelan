import tkinter as tk
from tkinter import messagebox

def login(user,password):
    master_data={'Oak':5101999}
    for users,keys in master_data.items:
        if users==user and keys==password:
            return messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
        else:
            return messagebox.showerror("Error", "Credenciales incorrectas")

root = tk.Tk()
root.title("Login")

label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(root)
entry_usuario.pack()

label_contrasena = tk.Label(root, text="Contraseña:")
label_contrasena.pack()
entry_contrasena = tk.Entry(root, show="*")  # Muestra asteriscos en lugar de la contraseña
entry_contrasena.pack()

boton_login = tk.Button(root, text="Iniciar sesión", command=login)
boton_login.pack()

root.mainloop()

#hola