import sqlite3

connection = sqlite3.connect('movies.db')
connection.execute('CREATE TABLE movies(name TEXT, description TEXT)')
print ('Table created successfully')

connection.close()
