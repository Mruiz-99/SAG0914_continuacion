import os
import psycopg2


def db_connection():
    conn = psycopg2.connect(
        database=os.getenv('PG_DATABASE'),
        host=os.getenv('PG_HOST'),
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASS'),
        port=os.getenv('PG_PORT')
    )

    print("Connection with postgres successfully")

    return conn.cursor()
