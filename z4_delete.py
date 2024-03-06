import sqlite3
conn= sqlite3.connect('databaseFile.db')
cr=conn.cursor()

cr.execute('DELETE FROM movies WHERE title=?;',('Inception',))
conn.commit() 
