from database.dbconnect import execute_a_query, fetch_from_db

def authn(email, password):
    query = f"SELECT password FROM clients WHERE email='{email}';"
    if password==fetch_from_db(query)[0][0]:
        return True
    return False


def add_client(email, name, address, password, phone):
    query2 = f'''select count(*) from clients where email='{email}';'''
    if int(fetch_from_db(query2)[0][0])>0:
        return (False, "Email already registered!")
    query1 = '''select count(*) from clients;'''
    c = int(fetch_from_db(query1)[0][0]) + 100000
    query = f"""INSERT INTO clients (name, email, address, phone, password) VALUES ('{name}', '{email}', '{address}', '{phone}', '{password}');"""
    execute_a_query(query)
    return (True, "User registered!")

