import sqlite3

DATABASE = "./first.db"


CREATE_BOOKS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS 
        books(
            id_book INTEGER,
            book_name VARCHAR(255),
            book_author VARCHAR(255),
            price NUMERIC
        )
    """

STATIC_INSERT_BOOKS_SQL = """
        INSERT INTO books VALUES 
        (1, 'Book 1', 'Book 1 Author', '400'),
        (2, 'Book 2', 'Book 2 Author', '500'),
        (3, 'Book 3', 'Book 3 Author', '600')
    """

INSERT_BOOKS_SQL = """
        INSERT INTO books VALUES
        ({id_book}, '{book_name}', '{book_author}', '{price}')
    """

SELECT_FROM_BOOKS_SQL = """ SELECT * FROM books """

SELECT_BOOK_NAME_AND_PRICE_BOOKS_SQL = """ SELECT book_name, price FROM books """

SELECT_FROM_BOOKS_LIMIT_SQL = """ SELECT * FROM books LIMIT 1 """

UPDATE_BOOK_SQL = """
    UPDATE books
    SET price='750' WHERE id_book=1
"""

DELETE_FROM_BOOKS_SQL = """
    DELETE FROM books WHERE id_book=1
"""


DROP_TABLE_BOOKS_SQL = """ DROP TABLE books """

with sqlite3.connect(DATABASE) as db:
    cursor = db.cursor()
    # cursor.execute(CREATE_BOOKS_TABLE_SQL)


# CRUD. C - Create. R - Read. U - Update, D - Delete
