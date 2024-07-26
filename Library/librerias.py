import tkinter as tk
from tkinter import messagebox,ttk
import sqlite3

def login(user,password):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("SELECT usuarioPsw FROM usuarios WHERE usuarioNombre = ?" , (user,))
    pw=cursor.fetchone()
    cursor.execute("CREATE TABLE IF NOT EXISTS sesion (sesionId INTEGER PRIMARY KEY AUTOINCREMENT,sesionNombre TEXT NOT NULL)")
    cursor.execute("INSERT INTO sesion (sesionNombre) VALUES (?)",(user,))
    bd.commit() 
    bd.close()
    return pw and pw[0]== password

def signup(user,password,rol):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("INSERT INTO usuarios (usuarioNombre, usuarioPsw, usuarioRol) VALUES (?, ?, ?)",(user,password,rol))
    bd.commit()
    bd.close()

def search_users():
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("SELECT (usuarioNombre,usuarioRol) FROM usuarios")
    search=cursor.fetchall()
    bd.close()
    return search

def recoger_sesion():
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("SELECT sesionNombre FROM sesion")
    sesion=cursor.fetchone()
    bd.close()
    return sesion

def drop_sesion():
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("DELETE FROM sesion")
    bd.commit()
    bd.close()

def create_pokemon(nombre, tipo, peso, altura, sexo, desc):
    try:
        bd = sqlite3.connect("Library/pokimons.db")
        cursor = bd.cursor()
        query = "INSERT INTO pokemons (pkNombre, pkTipo, pkPeso, pkAltura, pkSexo, pkDesc) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (nombre, tipo, peso, altura, sexo, desc))
        bd.commit()
        bd.close()
        return True
    except Exception as e:
        print(f"Error al crear el Pokémon: {e}")
        return False

def create_pokemon(nombre, tipo, peso, altura, sexo, desc):
    try:
        bd = sqlite3.connect("Library/pokimons.db")
        cursor = bd.cursor()
        query = "INSERT INTO pokemons (pkNombre, pkTipo, pkPeso, pkAltura, pkSexo, pkDesc) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (nombre, tipo, peso, altura, sexo, desc))
        bd.commit()
        bd.close()
        return True
    except Exception as e:
        print(f"Error al crear el Pokémon: {e}")
        return False
    

def update_pokemon(id, nombre, tipo, peso, altura, sexo, desc):
    try:
        bd = sqlite3.connect("Library/pokimons.db")
        cursor = bd.cursor()
        # Consulta para ver si existe el poke
        cursor.execute("SELECT pkId FROM pokemons WHERE pkId = ?", (id,))
        existing_pokemon = cursor.fetchone()
        if existing_pokemon:
            query = "UPDATE pokemons SET pkNombre = ?, pkTipo = ?, pkPeso = ?, pkAltura = ?, pkSexo = ?, pkDesc = ? WHERE pkId = ?"
            cursor.execute(query, (nombre, tipo, peso, altura, sexo, desc, id))
            print(f"Pokémon con ID {id} actualizado exitosamente.")
            bd.commit()
        else:
            print(f"Pokémon con ID {id} no existe.")
        
        bd.close()
        return True
    except Exception as e:
        print(f"Error al actualizar el Pokémon: {e}")
        return False


def delete_pokemon(id):
    try:
        bd = sqlite3.connect("Library/pokimons.db")
        cursor = bd.cursor()
        # Consulta para ver si existe el poke
        cursor.execute("SELECT pkId FROM pokemons WHERE pkId = ?", (id,))
        existing_pokemon = cursor.fetchone()
        if existing_pokemon:
            cursor.execute("DELETE FROM pokemons WHERE pkId = ?", (id,))
            print(f"Pokémon con ID {id} eliminado exitosamente.")
            bd.commit()
        else:
            print(f"Pokémon con ID {id} no existe.")
        bd.close()
        return True
    except Exception as e:
        print(f"Error al eliminar el Pokémon: {e}")
        return False