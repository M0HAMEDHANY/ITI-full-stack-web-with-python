import psycopg2
from psycopg2 import OperationalError


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="crowdfunding",
            user="", # user name
            password="", # password
            host="localhost",
            port="5432",
        )
        return conn
    except OperationalError as e:
        print(f"Error: {e}")
        return None



# if __name__ == "__main__":
#     connection = get_db_connection()
#     if connection:
#         print("Connection successful!")
#     else:
#         print("Failed to connect to the database.")
