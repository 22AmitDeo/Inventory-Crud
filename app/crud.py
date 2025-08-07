from sqlalchemy.orm import Session
from app import models, schemas

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# ✅ UPDATED FUNCTION
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if db_product:
        for field, value in product.dict().items():
            setattr(db_product, field, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

def create_stock_transaction(db: Session, tx: schemas.StockTransactionCreate):
    db_tx = models.StockTransaction(**tx.dict())
    product = get_product(db, tx.product_id)
    if tx.transaction_type == schemas.TransactionType.IN:
        product.available_quantity += tx.quantity
    elif tx.transaction_type == schemas.TransactionType.OUT:
        product.available_quantity -= tx.quantity
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx

def get_all_stock_transactions(db: Session):
    return db.query(models.StockTransaction).all()

def get_stock_transactions_for_product(db: Session, product_id: int):
    return db.query(models.StockTransaction).filter(models.StockTransaction.product_id == product_id).all()
