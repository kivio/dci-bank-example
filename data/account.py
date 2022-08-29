from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from .engine import Base

class Account(Base):
    __tablename__ = "accounts"
    account_id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    currency = Column(String)
    state = Column(String)
    balance = Column(Integer)
    owner_id = Column(ForeignKey("clients.client_id"))
    owner = relationship("Client", back_populates="accounts")

    __mapper_args__ = {
        "polymorphic_identity": "accounts", 
        "concrete": True,
    }