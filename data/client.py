from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from .engine import Base

class Client(Base):
    __tablename__ = "clients"
    client_id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    accounts = relationship("Account", back_populates="owner")