from fastapi import FastAPI, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List

from app import models, schemas, crud
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Product Endpoints ---

@app.post("/products/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.get("/products/", response_model=List[schemas.ProductOut])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip, limit=limit)

@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)

# --- Stock Transaction Endpoints ---

@app.post("/stock/", response_model=schemas.StockTransactionOut)
def create_stock_transaction(txn: schemas.StockTransactionCreate, db: Session = Depends(get_db)):
    return crud.create_stock_transaction(db, txn)

@app.get("/stock/", response_model=List[schemas.StockTransactionOut])
def read_stock_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_stock_transactions(db, skip=skip, limit=limit)

@app.get("/stock/product/{product_id}", response_model=List[schemas.StockTransactionOut])
def read_stock_by_product(product_id: int, db: Session = Depends(get_db)):
    return crud.get_stock_transactions_by_product(db, product_id)
