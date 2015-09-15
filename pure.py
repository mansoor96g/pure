
def connect(path):
    import sqlite3
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.text_factory = str
