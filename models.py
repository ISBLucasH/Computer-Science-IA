import sqlite3

def create_known_faces_table():
    connection = sqlite3.connect('site.db')
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