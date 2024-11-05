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

    insert_values = [(title, description, price) for title, description, price in [
        ('Product1', 'Описание: 1', 100),
        ('Product2', 'Описание: 2', 200),
        ('Product3', 'Описание: 3', 300),
        ('Product4', 'Описание: 4', 400),
    ]]
    cursor.executemany("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", insert_values)


    connection.commit()
    connection.close()

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
    
    
