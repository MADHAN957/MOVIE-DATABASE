import sqlite3

con = sqlite3.connect('Movies.db')
cur = con.cursor()

#run query to show all
cursor = cur.execute("SELECT * FROM MoviesINFO")
print('\n!---MoviesINFO all Rows and column data---!\n')
print(cur.fetchall())

# Query to fetch movies having release year 2018
cur.execute("SELECT * From MoviesINFO where ReleaseYear=2018")
print('\n!---MoviesINFO where ReleaseYear=2018---!\n')
print(cur.fetchall())

# Query to fetch only movie name and lead actor
cur.execute("SELECT Movie,LeadActor From MoviesINFO ")
print("\n!---QUery fetching only Movies name and lead Actor---!\n")
print(cur.fetchall())

con.commit()
con.close() 