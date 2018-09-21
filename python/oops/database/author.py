import sqlite3
db = sqlite3.connect('test.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY,
                    title TEXT, author TEXT, price TEXT, year TEXT)
               ''')
db.commit()
import sqlite3
db = sqlite3.connect('test.db')
cursor = db.cursor()
title1 = 'Learning Python'
author1 = 'Mark Lutz'
price1 = '$36.19'
year1 ='Jul 6, 2013'
 
title2 = 'Two Scoops of Django: Best Practices For Django 1.6'
author2 = 'Daniel Greenfeld'
price2 = '$34.68'
year2 = 'Feb 1, 2014'

cursor.execute('''INSERT INTO books(title, author, price, year)
                  VALUES(?,?,?,?)''', (title1, author1, price1, year1))

cursor.execute('''INSERT INTO books(title, author, price, year)
                   VALUES(?,?,?,?)''', (title2, author2, price2, year2))

db.commit()

