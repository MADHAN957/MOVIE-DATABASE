import sqlite3

#connect with database file
con= sqlite3.connect('Movies.db')
print(con)
print('you can see database opend!')
cur = con.cursor()

#create table name MoviesINFO
cur.execute('CREATE TABLE IF NOT EXISTS MoviesINFO(Movie VARCHAR,LeadActor TEXT,ReleaseYear INT,Director TEXT)')
print('Table created inside db')

#commit changes
con.commit()
#close connection
con.close()