import sqlite3
db = sqlite3.connect('data.db')
cursor = db.cursor()
#cursor.execute('''CREATE TABLE books(id INTEGER PRIMARY KEY, title TEXT, price TEXT,year TEXT)
#''')
#cursor.execute('''DROP TABLE books''')
title1 = 'Learning Python'
author1 = 'Mark Lutz'
price1 = '$36.19'
year1 ='Jul 6, 2013'
 
title2 = 'Two Scoops of Django: Best Practices For Django 1.6'
author2 = 'Daniel Greenfeld'
price2 = '$34.68'
year2 = 'Feb 1, 2014'
cursor.execute('''INSERT INTO books(id, title, price, year) VALUES(?,?,?,?)''', (title1, id, price1, year1))

cursor.execute('''INSERT INTO books(title, id, price, year)
                   VALUES(?,?,?,?)''', (title2, id, price2, year2))
db.commit()
db.close()
