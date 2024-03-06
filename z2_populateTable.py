import sqlite3
conn= sqlite3.connect('databaseFile.db')
cr=conn.cursor()

def add_movie(title, director, year, genre):
    cr.execute('''
        INSERT INTO movies(title, director, year, genre) 
        VALUES (?,?,?,?)''', (title, director, year, genre)
        )
    conn.commit()
    print("Movie Added :)")

add_movie('Inception', 'Christopher Nolan',2010,'Sci-Fi')
add_movie('The Shawshank Redemption', 'Frank Darabont', 1994, 'Drama')
add_movie('The Godfather', 'Francis Ford Coppola', 1972, 'Crime, Drama')
add_movie('Pulp Fiction', 'Quentin Tarantino', 1994, 'Crime, Drama')
add_movie('The Dark Knight', 'Christopher Nolan', 2008, 'Action, Crime, Drama')
add_movie('Forrest Gump', 'Robert Zemeckis', 1994, 'Drama, Romance')