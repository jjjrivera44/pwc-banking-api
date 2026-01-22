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
    if account_id is None:
        raise HTTPException(
            status_code=400, 
            detail="Error: Query parameter 'account_id' is required!"
        )

    # Logic: Query the actual database table we created in DBeaver
    try:
        with engine.connect() as connection:
            # Use text() to prevent SQL Injection (Managerial best practice)
            query = text("SELECT * FROM transactions WHERE account_id = :acc_id")
            result = connection.execute(query, {"acc_id": account_id})
            
            # Convert rows to a list of dictionaries for JSON response
            transactions = [dict(row._mapping) for row in result]

        if not transactions:
            raise HTTPException(
                status_code=404, 
                detail=f"No transactions found for account_id: {account_id}"
            )

        return transactions

    except Exception as e:
        # Useful for debugging in Render logs
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")