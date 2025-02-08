import sqlite3

connection_obj = sqlite3.connect('users.db')

cursor_obj = connection_obj.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS")

table = """ CREATE TABLE USERS (email VARCHAR 255 NOT NULL, password VARCHAR 255 NOT NULL)"""

cursor_obj.execute(table)

print("Table is ready")

connection_obj.close()
