import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = db.create_engine('sqlite:///bank.db')
connection = engine.connect()
metadata = db.MetaData()
Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)