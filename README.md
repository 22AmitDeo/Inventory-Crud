#  Inventory Management API

This is a backend API for managing products and stock transactions in an inventory system. It is built using **FastAPI**, **SQLAlchemy**, **Alembic**, and **PostgreSQL**.

---

##  Approach

The API is structured with a clean separation of concerns:

- **Models** (SQLAlchemy ORM): Define `Product` and `StockTransaction` tables.
- **Schemas** (Pydantic): Ensure request validation and response formatting.
- **CRUD Functions**: Business logic is placed in `crud.py` to keep routes lean.
- **Routes**: Defined in `main.py` using FastAPI path operations.
- **Migrations**: Handled using Alembic.

###  Validation

- **Price** and **quantity** must be non-negative.
- Stock transactions only accept `IN` or `OUT` types and affect product quantity accordingly.
- Invalid operations are handled gracefully with error messages.

---

##  Setup Instructions

### 1. Clone and Setup
```bash
git clone <your_repo_url>
cd inventory-crud
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Linux/Mac
pip install -r requirements.txt
```
### 2. Configure Database
```bash
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@localhost/<database>"
```
### 3. Run Alembic Migrations
```bash
alembic upgrade head
```
### 4.Running the Application
```bash
uvicorn app.main:app --reload
http://127.0.0.1:8000/docs
```
