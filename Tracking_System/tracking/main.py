from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from fastapi.templating import Jinja2Templates
from tracking.database import get_db, Base, engine
from tracking.models import Category, Transaction
from tracking.schemas import (
    CategoryCreate, Category,
    TransactionCreate, Transaction,
    BalanceResponse, ExpenseByCategory
)
from tracking import crud
from tracking.crud import create_category, create_transaction, get_all_categories, get_all_transactions
from tracking.reports import get_balance, get_expenses_by_category_last_days
from tracking.utils import export_transactions_to_csv
import os


app = FastAPI(title="Expense Tracker API")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/categories/", response_model=Category)
def add_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_cat = crud.get_category_by_name(db, name=category.name)
    if db_cat:
        raise HTTPException(status_code=400, detail="Category already exists")
    return create_category(db=db, category=category)

@app.post("/transactions/", response_model=Transaction)
def add_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    # Проверяем существование категории
    cat = db.get(Category, transaction.category_id)
    if not cat:
        raise HTTPException(status_code=404, detail="Category not found")
    return create_transaction(db=db, transaction=transaction)

@app.get("/categories/", response_model=List[Category])
def read_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)

@app.get("/transactions/", response_model=List[Transaction])
def read_transactions(db: Session = Depends(get_db)):
    return get_all_transactions(db)

@app.get("/reports/balance", response_model=BalanceResponse)
def get_current_balance(db: Session = Depends(get_db)):
    balance = get_balance(db)
    return {"balance": balance}

@app.get("/reports/expenses-by-category", response_model=List[ExpenseByCategory])
def expenses_by_category(days: int = 30, db: Session = Depends(get_db)):
    if days < 1 or days > 365:
        raise HTTPException(status_code=400, detail="Days must be between 1 and 365")
    return get_expenses_by_category_last_days(db, days=days)

@app.get("/export/csv")
def export_csv(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    filepath = "exports/transactions.csv"
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    background_tasks.add_task(export_transactions_to_csv, db, filepath)
    return {"message": "Export started", "file": filepath}
































