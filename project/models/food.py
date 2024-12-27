from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from database.dbconnect import get_session
from datetime import date

Base = declarative_base()

class Food(Base):
    __tablename__ = 'meal'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    type = Column(VARCHAR)
    meal_type = Column(VARCHAR)
    calorie = Column(Integer)
    

def get_meal_by_meal_type(meal_type):
    session = get_session()
    return session.query(Food).filter(Food.meal_type == meal_type)

def get_meal_by_type(type, mealtype):
    session = get_session()
    return session.query(Food).filter(Food.type == type).filter(Food.meal_type == mealtype)

