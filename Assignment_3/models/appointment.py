from database.dbconnect import fetch_from_db, execute_a_query

def make_appointment(id, license, engine, tech, day):
    query2 = f"""SELECT count(*) FROM appointments WHERE (car_license_number = '{license}' OR car_engine_number = '{engine}') AND appointment_date='{day}'  """
    query1= f"""SELECT count(*) FROM appointments WHERE mechanic_id = '{tech}'  AND appointment_date='{day}' """
    if int(fetch_from_db(query2)[0][0])>0:
        return False, "Already made an appointment."
    elif int(fetch_from_db(query1)[0][0]) >= 5:
        return False, "technician Not available"
    query = f"""INSERT INTO appointments (client_id, car_license_number, car_engine_number, mechanic_id, appointment_date) VALUES ('{id}', '{license}', '{engine}', '{tech}', '{day}' )"""
    execute_a_query(query)

    return True, "Appointment successfully booked!"





    