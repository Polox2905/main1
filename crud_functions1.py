import sqlite3


def initiate_db():
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        price INTEGER NOT NULL
    )
    ''')

    create_table_users(cursor)

    insert_values = [(title, description, price) for title, description, price in [
        ('Product1', 'Описание: 1', 100),
        ('Product2', 'Описание: 2', 200),
        ('Product3', 'Описание: 3', 300),
        ('Product4', 'Описание: 4', 400),
    ]]
    cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", insert_values)

    connection.commit()
    connection.close()


def create_table_users(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL DEFAULT 1000
    )
    ''')


def add_user(username, email, age):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    if is_included(username):
        raise ValueError(f"Пользователь с именем {username} уже существует.")

    cursor.execute("INSERT INTO Users (username, email, age) VALUES (?, ?, ?)", (username, email, age))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM Users WHERE username=?", (username,))
    count = cursor.fetchone()[0]

    connection.close()
    return bool(count)


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    select_query = "SELECT id, title, description, price FROM Products;"
    cursor.execute(select_query)
    records = cursor.fetchall()

    products = []
    for record in records:
        product = {'id': record[0], 'title': record[1], 'description': record[2], 'price': record[3]}
        products.append(product)
    return products


if __name__ == '__main__':
    initiate_db()
    all_products = get_all_products()
    print(all_products)