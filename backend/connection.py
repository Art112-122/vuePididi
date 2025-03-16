import sqlite3


def get_db_connection():
    connection = sqlite3.connect("users.db", timeout=5)
    connection.row_factory = sqlite3.Row
    return connection


def create_user_table():
    try:
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute("""
            CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            username TEXT NOT NULL UNIQUE,
            gmail TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            email_verified BOOLEAN DEFAULT FALSE);""")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error {e}")
    finally:
        conn.close()


def create_card_info_table():
    try:
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute("""
            CREATE TABLE IF NOT EXISTS card_info (
            card_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            first_name TEXT NOT NULL UNIQUE,
            second_name TEXT NOT NULL UNIQUE,
            card_number INTEGER NOT NULL,
            cvv_cod INTEGER NOT NULL,
            tame_date INTEGER NOT NULL);""")
        conn.commit()
    except sqlite3.Error as e:
        error_message = str(e).lower()
        if "unique constraint" in error_message:
            if "name" in error_message:
                print("Error: Duplicate card name found")
            elif "number" in error_message:
                print("Error: Duplicate card number found")
        else:
            print(f"Database error: {e}")
    finally:
        conn.close()



def create_user_settings_table():
    try:
        conn = get_db_connection()
        curs = conn.cursor()
        curs.execute("""
            CREATE TABLE IF NOT EXISTS users_settings (
            user_settings_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            color TEXT NOT NULL UNIQUE,
            language TEXT NOT NULL UNIQUE,);""")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error {e}")
    finally:
        conn.close()


def create_tables():
    create_card_info_table()
    create_user_table()
    create_card_info_table()
