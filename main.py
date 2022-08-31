
from data.client import Client
from data.account import Account
from domain.accounts import SenderAccount, ReciverAccount
from domain.currency import Currency
from context.transaction import Transaction
from interactions import transfer
from data.engine import Session, initiate_tables

print("Hello world")

with Session() as session:

    initiate_tables()

    sender = Client(first_name = "Marcin", last_name = "Karkocha")
    reciver = Client(first_name = "Aleksander", last_name = "Smok")

    session.add(sender)
    session.add(reciver)
    session.flush()

    sender_account = Account(
        name="Marcin's Account", 
        type="Main", 
        currency="PLN", 
        state="Open", 
        balance=500, 
        owner_id=sender.client_id
    )
    reciver_account = Account(
        name="Olek's Account", 
        type="Saving", 
        currency="PLN", 
        state="Open", 
        balance=0, 
        owner_id=reciver.client_id
    )

    session.add(sender_account)
    session.add(reciver_account)
    session.commit()
    
    marcin_account = SenderAccount(sender_account)
    olek_account = ReciverAccount(reciver_account)

    transaction = Transaction(
                    sender=marcin_account,
                    reciver=olek_account, 
                    currency=Currency("PLN")
                  )

    transfer(transaction, 200)
    
    print(marcin_account.balance)
    print(olek_account.balance)