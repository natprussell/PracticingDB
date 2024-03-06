import sqlite3
conn= sqlite3.connect('databaseFile.db')
cr=conn.cursor()

#uses database file specified with cr
#pulls list of all tables in listed database
cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cr.fetchall()
print(tables)

cr.execute("SELECT * FROM movies")
print(cr.fetchall())