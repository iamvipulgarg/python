import sqlite3
print(sqlite3.sqlite_version)

con = sqlite3.connect('mydb.db')
cur = con.cursor()
# cur.execute('CREATE TABLE USERS (id INTEGER, name TEXT)')

# query = "insert into USERS (id,name) VALUES (2,'VIPUL')"
# cur.execute(query)
# con.commit()
cur.execute('SELECT * FROM USERS')
results=cur.fetchall()
print(results)