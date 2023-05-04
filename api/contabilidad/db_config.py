"""import psycopg2
import os

# Conexion a la base de datos PostgreSQL
conn = psycopg2.connect(
    dbname = 'railway',
    user = 'postgres',
    password = 'P4NwoYhnRQwy5MjIwg1Y',
    host = 'containers-us-west-137.railway.app',  
    port = 5693
)
"""
"""conn = psycopg2.connect(
    dbname = os.getenv('PG_DATABASE'),
    user = os.getenv('PG_USER'),
    password = os.getenv('PG_PASS'),
    host = os.getenv('PG_HOST'),  
    port = os.getenv('PG_PORT')
)"""