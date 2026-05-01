from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas
from database import engine, get_db

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Add Income (Top-up)
@app.post("/transactions/income", response_model=schemas.TransactionResponse)
def add_income(data: schemas.IncomeCreate, db: Session = Depends(get_db)):
    transaction = models.Transaction(
        type="income",
        amount=data.amount,
        description=data.description,
        date=data.date
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


# 🔴 Add Expense
@app.post("/transactions/expense", response_model=schemas.TransactionResponse)
def add_expense(data: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    transaction = models.Transaction(
        type="expense",
        amount=data.amount,
        category=data.category,
        description=data.description,
        date=data.date
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


#  Get All Transactions (for testing)
@app.get("/transactions", response_model=list[schemas.TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()