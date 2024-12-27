from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = 'sqlite:///database/database.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()