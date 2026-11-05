import sqlite3

DB_NAME = "Faces.db"

def connect_db():
    connection = sqlite3.connect(DB_NAME)
    return connection

def create_known_faces_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS known_faces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        
        )
    ''')

    connection.commit()
    connection.close()


def get_known_faces():
    connection = sqlite3.connect('site.db')
    cursor = connection.cursor()