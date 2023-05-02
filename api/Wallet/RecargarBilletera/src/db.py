import psycopg2
import os

# Conexion a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname = os.getenv('PG_DATABASE'),
    user = os.getenv('PG_USER'),
    password = os.getenv('PG_PASS'),
    host = os.getenv('PG_HOST'),
    port = os.getenv('PG_PORT') 
)


