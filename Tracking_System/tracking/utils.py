import csv
from sqlalchemy.orm import Session
from tracking.models import Transaction, Category

def export_transactions_to_csv(db: Session, filepath: str):
    transactions = db.query(Transaction).all()
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Type", "Amount", "Category", "Description", "Date"])
        for t in transactions:
            writer.writerow([
                t.id,
                t.type.value,
                t.amount,
                t.category.name if t.category else "N/A",
                t.description or "",
                t.created_at.isoformat()
            ])
