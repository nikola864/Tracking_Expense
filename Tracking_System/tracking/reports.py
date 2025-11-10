from sqlalchemy import select, func
from sqlalchemy.orm import Session
from tracking.models import Transaction, Category
from datetime import datetime, timedelta
from tracking.schemas import ExpenseByCategory

def get_balance(db: Session) -> float:
    income = db.scalar(
        select(func.sum(Transaction.amount).where(Transaction.type == "income"))
    ) or 0.0

    expense = db.scalar(
        select(func.sum(Transaction.amount).where(Transaction.type == "expense"))
    ) or 0.0
    return round(income-expense, 2)

def get_expenses_by_category_last_days(db: Session, days: int = 30):
    since = datetime.utcnow() - timedelta(days=days)
    stmt = (
        select(Category.name, func.sum(Transaction.amount).label("total"))
        .select_from(Transaction)
        .join(Category)
        .where(Transaction.type == "expense", Transaction.created_at >= since)
        .group_by(Category.name)
    )
    result = db.execute(stmt).all()
    return [ExpenseByCategory(category=row[0], total=round(row[1], 2)) for row in result]