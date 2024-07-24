import tkinter as tk
from tkinter import messagebox,ttk
import sqlite3

def login(user,password):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("SELECT usuarioPsw FROM usuarios WHERE usuarioNombre = ?" , (user,))
    pw=cursor.fetchone()
    cursor.executescript('''
                         CREATE TABLE IF NOT EXISTS sesion (
                        sesionId INTEGER PRIMARY KEY AUTOINCREMENT,
                        sesionNombre TEXT NOT NULL
                        );
                        INSERT INTO sesion (sesionNombre) VALUES (?)
                         ''',(pw,))
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