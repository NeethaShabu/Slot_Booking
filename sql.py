import sqlite3

with sqlite3.connect("signup.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE Person3(Name TEXT , MailID TEXT, Pass TEXT)""")
	c.execute('INSERT INTO person3 VALUES("Sam","Sam@gmail.com", "Sam@123")')
	c.execute('INSERT INTO person3 VALUES("Maya","Maya@gmail.com","Maya12")')