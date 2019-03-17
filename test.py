import sqlite3

WALL_DB_PATH = 'data/thewall.db'

class User():
	def __init__(self):
		self.connection = sqlite3.connect(WALL_DB_PATH)
		self.cursor = self.connection.cursor()



	def get_user(self, username):
		query = "SELECT user_id from users WHERE username == ?"
		self.cursor.execute(query, (username,))
		user = self.cursor.fetchone()
		return user[0]

u = User()
print(u.get_user("Frank"))