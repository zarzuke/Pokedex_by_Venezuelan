import sqlite3

# Conectar a la base de datos
def connect():
    conn = sqlite3.connect('Library/pokimons.db')
    return conn

# Crear un nuevo Pokémon
def create_pokemon(pkNombre, pkTipo, pkPeso, pkAltura, pkSexo, pkDesc):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pokemons (pkNombre, pkTipo, pkPeso, pkAltura, pkSexo, pkDesc)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (pkNombre, pkTipo, pkPeso, pkAltura, pkSexo, pkDesc))
    conn.commit()
    conn.close()

# Leer todos los Pokémon
def read_pokemons():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT usuarioNombre, usuarioPsw FROM usuarios WHERE usuarioNombre == ? and usuarioPsw == ?
        ''')
    pokemons = cursor.fetchall()
    conn.close()
    return pokemons

# Actualizar un Pokémon
def update_pokemon(pkId, pkNombre, pkTipo, pkPeso, pkAltura, pkSexo, pkDesc):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE pokemons
        SET pkNombre = ?, pkTipo = ?, pkPeso = ?, pkAltura = ?, pkSexo = ?, pkDesc = ?
        WHERE pkId = ?
    ''', (pkNombre, pkTipo, pkPeso, pkAltura, pkSexo, pkDesc, pkId))
    conn.commit()
    conn.close()

# Eliminar un Pokémon
def delete_pokemon(pkId):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pokemons WHERE pkId = ?', (pkId,))
    conn.commit()
    conn.close()