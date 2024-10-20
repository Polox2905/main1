import sqlite3


connection = sqlite3.connect("not_telegram.db")
cursor=connection.cursor()



cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

data = [
    ("User1", "example1@gmail.com", 10, 1000),
    ("User2", "example2@gmail.com", 20, 1000),
    ("User3", "example3@gmail.com", 30, 1000),
    ("User4", "example4@gmail.com", 40, 1000),
    ("User5", "example5@gmail.com", 50, 1000),
    ("User6", "example6@gmail.com", 60, 1000),
    ("User7", "example7@gmail.com", 70, 1000),
    ("User8", "example8@gmail.com", 80, 1000),
    ("User9", "example9@gmail.com", 90, 1000),
    ("User10", "example10@gmail.com", 100, 1000)
]
#for username, email, age, balance in data:
#    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, balance))

#cursor.execute("UPDATE Users SET balance=500 WHERE ROWID % 2 == 0", [])

#cursor.execute("DELETE FROM Users WHERE ROWID % 3 == 1", [])

#cursor.execute("DELETE FROM Users WHERE ROWID  == 6", [])

query = "SELECT *  FROM Users"
result = cursor.execute(query).fetchall()
for row in result:
   print(f"Имя: {row[1]} | Почта: {row[2]} | Возраст: {row[3]} | Баланс: {row[4]}")

cursor.execute("SELECT COUNT(*) FROM Users")
total = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
total_count = cursor.fetchone()[0]
print(total_count/total)

cursor.close()
connection.commit()
connection.close()