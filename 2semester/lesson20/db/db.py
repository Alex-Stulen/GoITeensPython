import sqlite3

DATABASE_PATH = "./bot.db"


def connect_db():
    global DATABASE_PATH
    return sqlite3.connect(DATABASE_PATH)


def create_user_table():
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            first_name VARCHAR(64) NOT NULL,
            last_name VARCHAR(128),
            phone_number VARCHAR(14)
        ) """)


def get_all_users():
    with connect_db() as connection:
        cursor = connection.cursor()
        users_cursor = cursor.execute(""" SELECT * FROM USERS """)
        return users_cursor.fetchall()


def get_table_last_id(table_name: str) -> int:
    with connect_db() as connection:
        cursor = connection.cursor()

        # поганий варіант:
        data = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
        if data:
            last_row = data[-1]
            return last_row[0]
        else:
            return 0


def create_user(first_name: str, last_name: str = "", phone_number: str = ""):
    last_id = get_table_last_id("users")
    next_id = last_id + 1

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(f"""
            INSERT INTO users VALUES ({next_id}, "{first_name}", "{last_name}", "{phone_number}")
         """)


def get_users_by_first_name(first_name: str):
    with connect_db() as connection:
        cursor = connection.cursor()
        return cursor.execute(f""" SELECT * FROM users WHERE first_name = "{first_name}" """).fetchall()


def user_exist_by_first_name(first_name: str) -> bool:
    return bool(get_users_by_first_name(first_name))
