from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class TransactionType(str, Enum):
    income = "income"
    expense = "expense"

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class TransactionBase(BaseModel):
    amount: float
    type: TransactionType
    category_id: int
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class BalanceResponse(BaseModel):
    balance: float

class ExpenseByCategory(BaseModel):
    category: str
    total: float
    























