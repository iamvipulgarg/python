import mysql.connector

con=mysql.connector.connect(host="localhost",port="3306",user="root",password="",db="kelltron_filamnent")
cur=con.cursor()
# Fetch data from DB 
sel = "select id,title from products"
cur.execute(sel)
data=cur.fetchall()
print(data)
"""
title = input("Enter title : ")
shrt_desc = input("Enter Short DESC : ")
desc = input("Enter DESC : ")
img_path = input("Enter IMG Path : ")

# Insert Data in DB
q="insert into products (title,short_description,image,description) values ('{}','{}','{}','{}')".format(title,shrt_desc,img_path,desc)
cur.execute(q)
con.commit()

cur.execute(sel)
data=cur.fetchall()
print(data)
"""

# Update 
# title = input("Enter title for update : ")
# q="update products SET title = '{}' where id = 7".format(title)
# cur.execute(q)
# con.commit()

# cur.execute(sel)
# data=cur.fetchall()
# print(data)


# Delete
id=7
q="delete from products where id = '{}'".format(id)
cur.execute(q)
con.commit()

cur.execute(sel)
data=cur.fetchall()
print(data)
