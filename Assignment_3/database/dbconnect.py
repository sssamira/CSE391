import sqlite3
import os
location = os.path.abspath(os.path.join(os.path.dirname(__file__), '../database/workshop.db'))
def db_connection():
    conn = sqlite3.connect(location)
    conn.row_factory = sqlite3.Row  
    return conn

def execute_a_query(query):
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def fetch_from_db(query):
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result