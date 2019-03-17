import sqlite3

WALL_DB_PATH = 'data/thewall.db'

class Message():
	def __init__(self):
		self.connection = sqlite3.connect(WALL_DB_PATH)
		self.cursor = self.connection.cursor()

	def add_message(self, text, username):
		query = "INSERT INTO messages(text, username) VALUES(?, ?)"
		self.cursor.execute(query, (text, username))
		self.connection.commit()

	def get_messages(self):
		query = "SELECT * FROM messages ORDER BY id DESC"
		self.cursor.execute(query)
		messages = []
		for message in self.cursor.fetchall():
			message = {
				'username': message[2],
				'text': message[1]
			}
			messages.append(message)
		return messages

	def close(self):
		self.connection.close()