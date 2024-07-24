import tkinter as tk
from tkinter import messagebox,ttk
from test import login
import sqlite3

def login(user,password):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("SELECT usuarioPsw FROM usuarios WHERE usuarioNombre = ?" , (user,))
    pw=cursor.fetchone()
    bd.close()
    return pw and pw[0]== password

def signup(user,password,rol):
    bd = sqlite3.connect("Library/pokimons.db")
    cursor = bd.cursor()
    cursor.execute("INSERT INTO usuarios (usuarioNombre, usuarioPsw, usuarioRol) VALUES (?, ?, ?)",(user,password,rol))
    bd.commit()
    bd.close()

def search_users():
    cursor.execute("SELECT (usuarioNombre,usuarioRol) FROM usuarios")
    return cursor.fetchall()