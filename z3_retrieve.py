import sqlite3
conn= sqlite3.connect('databaseFile.db')
cr=conn.cursor()

#uses database file specified with cr
#pulls list of all tables in listed database
cr.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cr.fetchall()
print("list of tables in the DB file", tables,"\n")

#found out table name is movies
#this will pull all the columns from that table
cr.execute('PRAGMA table_info({})'.format('movies'))
columns=cr.fetchall()
column_Names=[column[1] for column in columns]
print('list of columns in the movie table\n.',column_Names,'\n')

cr.execute("SELECT * FROM movies")
print(cr.fetchall())