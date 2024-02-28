import sqlite3
conn= sqlite3.connect('databaseFile.db')
cr=conn.cursor()

cr.execute('''
           CREATE TABLE IF NOT EXISTS movies (
           id INTEGAR PRIMARY KEY,
           title TEXT,
           director TEXT,
           year INTEGAR,
           genre TEXT)
           ''')

# be sure to include SQL code for columns in additional ()
# table should be created with attributes and columns 