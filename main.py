<<<<<<< HEAD
import os
from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from sqlalchemy import create_engine, text

app = FastAPI(title="PwC Banking Transactions API")

# --- DATABASE SETUP ---
DATABASE_URL = os.getenv("DATABASE_URL")

# Fix for Render/SQLAlchemy compatibility
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)

@app.get("/")
def health_check():
    return {"status": "active", "message": "Banking API is running"}

@app.get("/transactions")
def get_transactions(account_id: Optional[int] = Query(None)):
    """
    Retrieves banking transactions for a specific account.
    """
    # 1. Acceptance Criteria: Error handling for missing account_id
    if account_id is None:
        raise HTTPException(
            status_code=400, 
            detail="Error: Query parameter 'account_id' is required!"
        )

    # 2. Logic: Query the PostgreSQL database
    transactions = []
    try:
        with engine.connect() as connection:
            # Note: We use :acc_id as a placeholder to prevent SQL Injection
            query = text("SELECT * FROM transactions WHERE account_id = :acc_id")
            result = connection.execute(query, {"acc_id": account_id})
            
            # Convert database rows into a list of dictionaries
            transactions = [dict(row._mapping) for row in result]
            
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # 3. Acceptance Criteria: Error handling for no transactions found
    if not transactions:
        raise HTTPException(
            status_code=404, 
            detail=f"No transactions found for account_id: {account_id}"
        )

    # 4. Success: Return the JSON results
    return transactions
=======
import os
from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from sqlalchemy import create_engine, text

app = FastAPI(title="PwC Banking Transactions API")

# --- DATABASE SETUP ---
DATABASE_URL = os.getenv("DATABASE_URL")

# Fix for Render/SQLAlchemy compatibility: 
# Render uses 'postgres://', SQLAlchemy 1.4+ requires 'postgresql://'
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Connect to the database
engine = create_engine(DATABASE_URL)

@app.get("/")
def health_check():
    return {"status": "active", "message": "Banking API is connected to Render Postgres"}

@app.get("/transactions")
def get_transactions(account_id: Optional[str] = Query(None)):
    """
    Retrieves banking transactions for a specific account from PostgreSQL.
    """
    # 1. Acceptance Criteria: Error handling for missing account_id
    if account_id is None:
        raise HTTPException(
            status_code=400, 
            detail="Error: Query parameter 'account_id' is required!"
        )

    # 2. Logic: Query the actual database table
    transactions = []
    try:
        with engine.connect() as connection:
            # Use text() to prevent SQL Injection
            query = text("SELECT * FROM transactions WHERE account_id = :acc_id")
            result = connection.execute(query, {"acc_id": account_id})
            
            # Convert rows to a list of dictionaries
            transactions = [dict(row._mapping) for row in result]
            
    except Exception as e:
        # Technical log for Render
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # 3. Acceptance Criteria: Error handling for no transactions found
    # (Checking this OUTSIDE the try block ensures the 404 is returned correctly)
    if not transactions:
        raise HTTPException(
            status_code=404, 
            detail=f"No transactions found for account_id: {account_id}"
        )

    # 4. Success: Return the JSON results
    return transactions
>>>>>>> 8956893 (Fix: Separated 404 logic from DB try-except block)
