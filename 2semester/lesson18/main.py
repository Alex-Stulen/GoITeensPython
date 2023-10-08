import sqlite3


DATABASE = "flowershop.db"


CREATE_WORKERS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS workers(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(64),
            surname VARCHAR(128),
            phone_number VARCHAR(14),
            working_rate DOUBLE
        );
    """

CREATE_WORKERS_SQL = """
        INSERT INTO workers VALUES 
        (1, 'John', 'Haws', '+3806877777777', 1),
        (2, 'Kate', 'Laws', '+3806866666666', 1),
        (3, 'John', 'Doe', '+3806833333333', 1)
    """

CREATE_MATERIALS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS materials(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(255),
            quantity_available INTEGER
        );
    """

CREATE_CLIENTS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(255),
            surname VARCHAR(128),
            phone_number VARCHAR(14)
        );
    """

CREATE_PRODUCTIVITY_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS productivity(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            month INTEGER,
            worker_id INTEGER REFERENCES workers(id),
            hours DOUBLE,
            order_quantity INTEGER
        );
    """

CREATE_SHIPPERS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS shippers(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name VARCHAR(255),
            contacts VARCHAR(512),
            material_id INTEGER REFERENCES materials(id),
            price NUMERIC
        );
    """

CREATE_ORDERS_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            worker_id INTEGER REFERENCES workers(id),
            client_id INTEGER REFERENCES clients(id),
            order_name VARCHAR(255),
            date TIMESTAMP,
            material_id INTEGER REFERENCES materials(id),
            costs NUMERIC
        );
    """


with sqlite3.connect(DATABASE) as db:
    cursor = db.cursor()

    sql1 = """
        INSERT INTO clients VALUES 
        (1, 'Andrew', 'Hollow', '+3806877777777'),
        (2, 'Alex', 'Wales', '+3806888888888'),
        (3, 'Arya', 'Walt', '+380689999999')
    """

    sql2 = """
        INSERT INTO workers VALUES
        (1, 'John', 'Hals', '+3806877777777', 1),
        (2, 'Kate', 'Laws', '+380689999999', 1.25)
    """

    # cursor.execute(sql1)
    # cursor.execute(sql2)

    clients = cursor.execute(""" SELECT * FROM clients LIMIT 3 """).fetchall()
    print(clients)
