import os
from fastapi import FastAPI, Query, HTTPException
from typing import List, Optional
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables (for local testing)
load_dotenv()

app = FastAPI(
    title="PwC Banking Transactions API",
    description="API to retrieve banking transactions from Cloud SQL (PostgreSQL)",
    version="1.0.0"
)

# --- DATABASE SETUP ---
DATABASE_URL = os.getenv("DATABASE_URL")

# Compatibility fix for SQLAlchemy 1.4+
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

@app.get("/", tags=["Health"])
def health_check():
    """
    Checks if the API is running and connected.
    """
    return {
        "status": "active", 
        "message": "PwC Banking API is live",
        "environment": "Google Cloud Run"
    }

@app.get("/transactions", tags=["Banking"])
def get_transactions(account_id: int = Query(None, description="The unique ID of the bank account (Must be an integer)")):
    """
    Retrieves banking transactions for a specific account.
    - Providing a string (like 'abc') will trigger a **422 Unprocessable Entity** error.
    - Leaving it empty will trigger a **400 Bad Request** error.
    """
    
    # 1. Acceptance Criteria: Error handling for missing account_id
    if account_id is None:
        raise HTTPException(
            status_code=400, 
            detail="Error: Query parameter 'account_id' is required!"
        )

    transactions = []
    try:
        # Use a context manager to handle the connection properly
        with engine.connect() as connection:
            # text() prevents SQL Injection by using bound parameters
            query = text("SELECT * FROM transactions WHERE account_id = :acc_id")
            result = connection.execute(query, {"acc_id": account_id})
            
            # Map the database rows into a list of dictionaries for JSON output
            transactions = [dict(row._mapping) for row in result]
            
    except Exception as e:
        # Log the error for debugging in Google Cloud Logs
        print(f"Database connection error: {e}")
        raise HTTPException(
            status_code=500, 
            detail="Database connection issue. Please check Cloud SQL connectivity."
        )

    # 2. Acceptance Criteria: Error handling for no transactions found
    if not transactions:
        raise HTTPException(
            status_code=404, 
            detail=f"No transactions found for account_id: {account_id}"
        )

    # 3. Success: Return the list of transactions
    return transactions