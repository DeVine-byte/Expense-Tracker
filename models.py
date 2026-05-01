from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  # "income" or "expense"
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=True)
    description = Column(String, nullable=True)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)