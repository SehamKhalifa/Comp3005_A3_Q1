import psycopg2

DATABASE = "A3_db"
USERNAME = "postgres"
PASSWORD = "Saym123"
HOST = "localhost"

def get_connection():
    return psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USERNAME,
        password=PASSWORD
    )
