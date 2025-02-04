import psycopg2



def create_table():
    try:
        conn = psycopg2.connect(
            dbname="your_db",
            user="your_user",
            password="your_password",
            host="localhost",
            port="5432",
            client_encoding="UTF8"
        )
        curs = conn.cursor()
        curs.execute("""CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT)""")
        conn.commit()
        curs.close()
        conn.close()
    except Exception as e:
        print("Ошибка подключения:", e)
create_table()
