import sqlite3


def get_db_connection():
    connection = sqlite3.connect("users.db", timeout=5)
    connection.row_factory = sqlite3.Row
    return connection


def connect_user_to_card(user_id, card_id, email, card_number, cvv_code):
    try:
        conn = get_db_connection()
        curs = conn.cursor()
        table_insert = f"""INSERT INTO Card (user_id, card_id, email, card_number, cvv_code)
            VALUES ({user_id}, {card_id}, {email}, {card_number}, {cvv_code});"""
        curs.execute(table_insert)
    except sqlite3.Error as error:
        print(f"Error: {error}")
    finally:
        curs.close()
        conn.close()


def create_user_table():
    try:
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute("""
            CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            gmail TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL);""")
        conn.commit()
    except sqlite3.Error as error:
        print(f"Error {error}")
    finally:
        conn.close()


def create_card_info_table():
    try:
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute("""
            CREATE TABLE IF NOT EXISTS card_info(
            user_id INTEGER UNIQUE NOT NULL,
            card_id INTEGER PRIMARY KEY UNIQUE,
            email TEXT NOT NULL UNIQUE,
            card_number INTEGER NOT NULL,
            cvv_code INTEGER  UNIQUE NOT NULL);""")
        conn.commit()
    except sqlite3.Error as e:
        error_message = str(e).lower()
        if "unique constraint" in error_message:
            if "name" in error_message:
                print("Error: Duplicate card name found")
            elif "number" in error_message:
                print("Error: Duplicate card number found")
        else:
            print(f"Card database error: {e}")
    finally:
        conn.close()


def select_card_query(where: str | None = "", select: str | None = "*"):
    conn = get_db_connection()

    curs = conn.cursor()

    query = f"""SELECT {select} FROM Cards {where}"""
    curs.execute(query)

    if " " in select or select == "*":
        result = curs.fetchall()
    else:
        result = curs.fetchone()

    curs.close()
    conn.commit()
    conn.close()
    return result


def select_user_query(where: str | None = "", select: str | None = "*"):
    conn = get_db_connection()

    curs = conn.cursor()

    query = f"""SELECT {select} FROM Users {where}"""
    curs.execute(query)
    if " " in select or select == "*":
        result = curs.fetchall()
    else:
        result = curs.fetchone()
    curs.close()
    conn.commit()
    conn.close()
    return result


def create_tables():
    create_card_info_table()
    create_user_table()
