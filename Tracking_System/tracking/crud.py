from sqlalchemy.orm import Session
from tracking.models import Category, Transaction, TransactionType
from tracking.schemas import CategoryCreate, TransactionCreate

def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name = category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def create_transaction(db: Session, transaction: TransactionCreate):
    db_trans = Transaction(**transaction.model_dump())
    db.add(db_trans)
    db.commit()
    db.refresh(db_trans)
    return db_trans

def get_all_categories(db: Session):
    return db.query(Category).all()

def get_all_transactions(db: Session):
    return db.query(Transaction).all()