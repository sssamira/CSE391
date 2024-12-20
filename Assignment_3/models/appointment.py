from database.dbconnect import *

def make_appointment(id, license, engine, tech, day):
    query2 = f"""SELECT count(*) FROM appointments WHERE (car_license_number = '{license}' OR car_engine_number = '{engine}') AND appointment_date='{day}'  """
    query1= f"""SELECT count(*) FROM appointments WHERE mechanic_id = '{tech}'  AND appointment_date='{day}' """
    if int(fetch_from_db(query2)[0][0])>0:
        return False, "Already made an appointment."
    elif int(fetch_from_db(query1)[0][0]) >=4:
        return False, "technician Not available"
    query = f"""INSERT INTO appointments (client_id, car_license_number, car_engine_number, mechanic_id, appointment_date) VALUES ('{id}', '{license}', '{engine}', '{tech}', '{day}' )"""
    execute_a_query(query)

    return True, "Appointment successfully booked!"

def get_all_appointments():
    query = """SELECT a.*, m.name FROM appointments a INNER JOIN mechanics m ON a.mechanic_id = m.id"""

    return fetch_from_db(query)



def all_mechanics():
    query = f"""SELECT * FROM mechanics"""
    return fetch_from_db(query)

def free_slots(day, mechanic_id):
    query = f"""SELECT COUNT(*) FROM appointments WHERE mechanic_id = '{mechanic_id}' AND appointment_date = '{day}'"""
    return fetch_from_db(query)

def change_appointment(id, tech, day):
    data = free_slots(day, tech)
    if data[0][0]>= 4:
        return False, "Technician not available"
    query = f"""UPDATE appointments SET mechanic_id = '{tech}', appointment_date = '{day}' WHERE id = '{id}'"""
    execute_a_query(query)
    return True, "Appointment successfully updated!"