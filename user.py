import sqlite3

WALL_DB_PATH = 'data/thewall.db'

class User():
	def __init__(self):
		self.connection = sqlite3.connect(WALL_DB_PATH)
		self.cursor = self.connection.cursor()

	def login(self, username, password):
		query = "SELECT * from users WHERE username == ? AND password == ?"
		self.cursor.execute(query, (username, password))
		user = self.cursor.fetchone()
		if user is not None:
			return True
		else:
			return False
		self.connection.close()

	def signup(self, username, password):
		query = "INSERT INTO users (username, password) VALUES (?, ?)"
		self.cursor.execute(query, (username, password))
		self.connection.commit()
		self.connection.close()
