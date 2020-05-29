import sqlite3

conn = sqlite3.connect("database.db")
#conn.execute("CREATE TABLE user (username TEXT, password TEXT);")
conn.execute("INSERT INTO user (username, password) VALUES ('jorge', '1234')")
conn.commit()

print("sucess")
conn.close()