import sqlite3

conn = sqlite3.connect('hoops.sqlite')
cur = conn.cursor()

first_name = input("Enter a player's first name: ")
last_name = input("Enter a player's last name: ")
team = input("Enter a player's team: ")

# cur.execute('''CREATE TABLE PLAYERS(first_name varchar,
									# last_name varchar,
									# team varchar)''')

cur.execute('''INSERT INTO PLAYERS (first_name, last_name, team)
VALUES (?,?,?)''', (first_name, last_name, team))

conn.commit()
	 
cur.close()