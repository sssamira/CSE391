from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from database.dbconnect import get_session
from datetime import date

Base = declarative_base()


class Exercise(Base):
    __tablename__ = 'exercise'

    exercise_id = Column(Integer, primary_key=True) 
    exercise_type = Column(String(10))  
    exercise_name = Column(String(50))  
    target_area = Column(String(50))  
    perhour_calorie_burn = Column(Float) 
    step = Column(Text) 
    gif = Column(String(255))

def get_exerciseby_typ(type):
    session = get_session()
    return session.query(Exercise).filter(Exercise.exercise_type == type).all()

def get_all_exercise():
    session = get_session()
    return session.query(Exercise).all()


