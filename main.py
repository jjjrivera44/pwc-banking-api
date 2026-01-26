import os
from typing import List, Optional
from fastapi import FastAPI, Query, HTTPException
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()

app = FastAPI(title="PwC Banking Transactions API")

# 2. Database Connection Logic
DATABASE_URL = os.getenv("DATABASE_URL")

# Compatibility Fix for Render/GCP
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

if not DATABASE_URL:
    print("CRITICAL ERROR: DATABASE_URL not set.")
else:
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

@app.get("/")
def health_check():
    return {"status": "active", "message": "API is online and using Integer Account IDs"}

@app.get("/transactions")
def get_transactions(account_id: Optional[int] = Query(None)):
    """
    Retrieves transactions for a specific account.
    FastAPI will now automatically validate that 'account_id' is an integer.
    """
    # Acceptance Criteria: Required field check
    if account_id is None:
        raise HTTPException(
            status_code=400, 
            detail="Error: Query parameter 'account_id' is required and must be an integer."
        )

    transactions = []
    try:
        with engine.connect() as connection:
            # The :acc_id parameter will now safely handle the integer value
            query = text("SELECT transaction_id, account_id, amount, merchant, description, date, type FROM transactions WHERE account_id = :acc_id")
            result = connection.execute(query, {"acc_id": account_id})
            
            # Map rows to dictionaries
            transactions = [dict(row._mapping) for row in result]
            
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    # Acceptance Criteria: 404 for no results
    if not transactions:
        raise HTTPException(
            status_code=404, 
            detail=f"No transactions found for account_id: {account_id}"
        )

    return transactions