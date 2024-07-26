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
    
    
    
#Funciones Para Lista Pokemons
def search_pk(pokemon):
        bd = sqlite3.connect("Library/pokimons.db")
        cursor = bd.cursor()
        if pokemon:
            for pk in pokemon:
                cursor.execute("""
                    SELECT p.pkId,p.pkNombre,t.tipoNombre,p.pkPeso,p.pkAltura,s.sexoNombre,p.pkDesc FROM pokemons as p
                    INNER JOIN tipos as t ON pkTipo == tipoId
                    INNER JOIN sexo as s ON pkSexo == sexoId
                    WHERE p.pkNombre == ?
                    """,(pk,))
                search=cursor.fetchall()
            return search
        else:
            search = None
            return search
        bd.close()
        
#funcion sql para buscar datos del pokemon especifico
def search_pk_fav(pokemon):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    search=[]
    if pokemon:
        for pk in pokemon:
            cursor.execute("""
                SELECT p.pkId,p.pkNombre,t.tipoNombre,p.pkPeso,p.pkAltura,s.sexoNombre,p.pkDesc FROM pokemons as p
                INNER JOIN tipos as t ON pkTipo == tipoId
                INNER JOIN sexo as s ON pkSexo == sexoId
                WHERE p.pkNombre == ?
                """,(pk,))
            search.append(cursor.fetchall())
        return search
    else:
        return search
    bd.close()

#funcion sql para recoger info de todos los pokemons
def search_all_pk():
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("""
        SELECT p.pkId,p.pkNombre,t.tipoNombre,p.pkPeso,p.pkAltura,s.sexoNombre,p.pkDesc FROM pokemons as p
        INNER JOIN tipos as t ON pkTipo == tipoId
        INNER JOIN sexo as s ON pkSexo == sexoId
        ORDER BY p.pkId ASC
        """)
    search=cursor.fetchall()
    bd.close()
    return search

def save_pk(username,pks):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = db.cursor()
    cursor.execute("UPDATE usuarios SET usuarioPkF == ? WHERE usuarioNombre == ?",(pks,username))
    db.commit()
    db.close() 
            
def search_favorite_pk(username):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = db.cursor()
    cursor.execute('SELECT usuarioPkF FROM usuarios WHERE usuarioNombre == ?',(username,))
    search = cursor.fetchone()
    return search