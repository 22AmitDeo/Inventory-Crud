from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import enum

class TransactionType(str, enum.Enum):
    IN = "IN"
    OUT = "OUT"

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: float = Field(ge=0)
    available_quantity: int = Field(ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    class Config:
        orm_mode = True

class StockTransactionBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    transaction_type: TransactionType

class StockTransactionCreate(StockTransactionBase):
    pass

class StockTransactionOut(StockTransactionBase):
    id: int
    timestamp: datetime
    class Config:
        orm_mode = True
