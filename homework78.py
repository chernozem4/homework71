import sqlite3

def database():
    conn = sqlite3.connect('ABOBA.db')
    number = conn.cursor()
    number.execute('''CREATE TABLE IF NOT EXISTS products 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 product TEXT NOT NULL,
                 price REAL NOT NULL DEFAULT 0.0,
                 quantity INTEGER NOT NULL DEFAULT 0)''')
    conn.commit()
    conn.close()

def add_products():
    products = [
        ("товар 1", 10.25, 30),
        ("товар 2", 1.5,30),
        ("товар 3", 3.5, 100),
        ("товар 4", 15.45, 20),
        ("товар 5", 8.2, 10),
        ("товар 6", 34.4, 50),
        ("товар 7", 15.4, 150),
        ("товар 8", 90.9, 250),
        ("товар 9", 99.99, 350),
        ("товар 10", 99.99, 450),
        ("товар 11", 24.34, 630),
        ("товар 12", 6.2, 70),
        ("товар 13", 90.2, 80),
        ("14", 90.2, 56),
        ("15", 13.9999, 111)
    ]
    conn = sqlite3.connect('ABOBA.db')
    number = conn.cursor()
    number.executemany("INSERT INTO products (product, price, quantity) VALUES (?,?,?)", products)
    conn.commit()
    conn.close()

def change_quantity(product_id, new_quantity):
    conn = sqlite3.connect('ABOBA.db')
    number = conn.cursor()
    number.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
    conn.commit()
    conn.close()

def change_price(product_id, new_price):
    conn = sqlite3.connect('ABOBA.db')
    number = conn.cursor()
    number.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('ABOBA.db')
    number = conn.cursor()
    number.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def select_all_products():
    conn = sqlite3.connect('ABOBA.db')
    number = conn.cursor()
    number.execute("SELECT * FROM products")
    products = number.fetchall()
    conn.close()
    return products

def select_products(price_limit, quantity_limit):
    conn = sqlite3.connect('ABOBA.db')
    number= conn.cursor()
    number.execute("SELECT * FROM products WHERE price < ? AND quantity > ?", (price_limit, quantity_limit))
    products = number.fetchall()
    conn.close()
    return products

def search_product(keyword):
    conn = sqlite3.connect('ABOBA.db')
    number = conn.cursor()
    number.execute("SELECT * FROM products WHERE product LIKE ?", ('%'+keyword+'%',))
    products = number.fetchall()
    conn.close()
    return products

database()
add_products()
print("Данные в БД")
print(select_all_products())
change_quantity(6, 25)
print("Изменение товара")
print(select_all_products())
change_price(4, 19.99)
print("Изменение цены")
print(select_all_products())
delete_product(6)
print("Удаление продукта")
print(select_all_products())
print("Продукты менее 20 монет и более 100")
print(select_products(20, 100))
print("Товары с названием 'товар'")
print(search_product('товар'))
