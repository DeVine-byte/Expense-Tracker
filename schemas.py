from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TransactionBase(BaseModel):
    amount: float
    description: Optional[str] = None
    date: datetime

class IncomeCreate(TransactionBase):
    pass

class ExpenseCreate(TransactionBase):
    category: str

class TransactionResponse(BaseModel):
    id: int
    type: str
    amount: float
    category: Optional[str]
    description: Optional[str]
    date: datetime

    class Config:
        from_attributes = True