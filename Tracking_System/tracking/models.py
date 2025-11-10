from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from tracking.database import Base
import enum

class TransactionType(str, enum.Enum):
    income = "income"       #доход
    expense = "expense"     #расход

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=False)
    amount = Column(Float, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    description = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
