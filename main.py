"""Transaction api for a personal finance manager"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Transaction(BaseModel):
    """Transaction class."""
    description: str
    amount: float
    date: str # maybe change this to a datetime obj

transactions = []

@app.post("/transactions/")
async def create_transaction(transaction: Transaction):
    """create a transaction and store in memory.

    Args:
        transaction: a class with transaction info.

    Returns:
        The transaction obj.
    """
    transactions.append(transaction)
    return transaction

@app.get("/transactions/")
async def get_transactions():
    """Return the list of transactions.

    Returns:
        A list of transactions.
    """
    return transactions
