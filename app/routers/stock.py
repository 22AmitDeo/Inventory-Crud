from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.StockTransactionOut)
def create_transaction(tx: schemas.StockTransactionCreate, db: Session = Depends(get_db)):
    return crud.create_stock_transaction(db, tx)

@router.get("/", response_model=list[schemas.StockTransactionOut])
def read_transactions(db: Session = Depends(get_db)):
    return crud.get_all_stock_transactions(db)

@router.get("/product/{product_id}", response_model=list[schemas.StockTransactionOut])
def read_transactions_for_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_stock_transactions_for_product(db, product_id)
