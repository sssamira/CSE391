from database.dbconnect import execute_a_query, fetch_from_db

def authn(email, password):
    query = f"SELECT email, password FROM clients WHERE email='{email}';"
    result = fetch_from_db(query)
    if len(result) == 0:
        return False
    if password==result[0][1]:
        return True
    return False



def add_client(email, name, address, password, phone):
    query2 = f'''select count(*) from clients where email='{email}';'''
    if int(fetch_from_db(query2)[0][0])>0:
        return (False, "Email already registered!")
    query = f"""INSERT INTO clients (name, email, address, phone, password, isadmin) VALUES ('{name}', '{email}', '{address}', '{phone}', '{password}', 'False');"""
    execute_a_query(query)
    return (True, "User registered!")

