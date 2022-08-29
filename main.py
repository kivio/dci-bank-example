from data.engine import Session
from data.client import Client
from data.account import Account

print("Hello world")

sender = Client(first_name = "Marcin", last_name = "Karkocha")
reciver = Client(first_name = "Aleksander", last_name = "Smok")

with Session() as session:
    session.add(sender)
    session.add(reciver)
    session.commit()
    