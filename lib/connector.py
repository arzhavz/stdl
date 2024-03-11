import sqlite3
import json
import random
import string


class Database:
	def __init__(self, db_name='user_data.db'):
		self.db_name = db_name
		self.create()

	@property
	def id(self):
		return '437b8465-252c-4fd4-a9e2-9122719bab9f' #id apa ajah

	def create_default_user_data(self, user_id):
		default_data = {
			"user": {
				"id": "User#" + user_id,
				"name": random.choice(["Sang Mitologi Jawa", "Pangeran Hitam Tanah Pasundan", "The Darkness of Child Molester", "Laskar Kegelapan", "Kesatria Berkuda", "Majestic of Child Predator"]),
				"theme": "Dark Default",
				"token": 0
			}
		}
		return default_data

	def create(self):
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()

		cursor.execute('''CREATE TABLE IF NOT EXISTS users (
						user_id TEXT PRIMARY KEY,
						data TEXT)''')

		conn.commit()
		conn.close()

	def read(self, user_id):
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()

		cursor.execute("SELECT data FROM users WHERE user_id=?", (user_id,))
		row = cursor.fetchone()

		if row:
			user_data = json.loads(row[0])
		else:
			user_data = self.create_default_user_data(user_id)
			cursor.execute("INSERT INTO users (user_id, data) VALUES (?, ?)", (user_id, json.dumps(user_data)))
			conn.commit()

		conn.close()
		return user_data

	def update(self, user_id, new_data):
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()

		cursor.execute("SELECT data FROM users WHERE user_id=?", (user_id,))
		row = cursor.fetchone()

		if row:
			old_data = json.loads(row[0])

			if "user" in new_data:
				old_data["user"].update(new_data["user"])
			elif "theme" in new_data:
				old_data["user"]["theme"] = new_data["theme"]
			elif "name" in new_data:
				old_data["user"]["name"] = new_data["name"]

			cursor.execute("UPDATE users SET data=? WHERE user_id=?", (json.dumps(old_data), user_id))

		conn.commit()
		conn.close()