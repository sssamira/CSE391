import sqlite3
import os
location = os.path.abspath(os.path.join(os.path.dirname(__file__), '../database/workshop.db'))
def db_connection():
    conn = sqlite3.connect(location) 
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

def get_userid(email):
    connection = db_connection()
    cursor = connection.cursor()
    query= f"""select id from clients where email='{email}';"""
    cursor.execute(query)
    result = cursor.fetchall()
    return result
def get_mecha_name(id):
    connection = db_connection()
    cursor = connection.cursor()
    query= f"""select name from mechanics where id='{id}';"""
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_role(id):
    connection = db_connection()
    cursor = connection.cursor()
    query= f"""select isadmin from clients where id='{id}';"""
    cursor.execute(query)
    result = cursor.fetchall()
    if result[0][0] == 'True':
        return True
    else:
        return False
    
def get_client_info(id):
    connection = db_connection()
    cursor = connection.cursor()
    query= f"""select name, phone from clients where id='{id}';"""
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_mecha_id(name):
    connection = db_connection()
    cursor = connection.cursor()
    query= f"""select id from mechanics where name='{name}';"""
    cursor.execute(query)
    result = cursor.fetchall()
    return result
