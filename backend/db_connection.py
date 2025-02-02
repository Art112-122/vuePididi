import psycopg2


def get_postgresql_connection():
    try:
        connection = psycopg2.connect(
            host="...",
            dbname="...",
            user="...",
            password="...",
            port=8080)
        curs = connection.cursor()
        return curs, connection
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None, None
