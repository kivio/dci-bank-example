import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = db.create_engine('sqlite:///bank.db')
connection = engine.connect()
metadata = db.MetaData()

def initiate_tables():
    Base.metadata.create_all(engine, Base.metadata.tables.values(), checkfirst=True)

Session = sessionmaker()
Session.configure(bind=engine)