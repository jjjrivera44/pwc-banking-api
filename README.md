# PwC Banking Transactions API

This repository contains a production-ready FastAPI application designed to retrieve banking transactions from a PostgreSQL database.

## 🚀 Live Deployment
- **API URL:** https://pwc-banking-api.onrender.com/transactions
- **Interactive Documentation:** https://pwc-banking-api.onrender.com/docs#/

## 🛠 Tech Stack
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **ORM:** SQLAlchemy (with Parameterized Queries for SQL Injection protection)
- **Database:** Managed PostgreSQL (Render)
- **Containerization:** Docker

## ✅ Features & Acceptance Criteria
- **Validation:** Enforces `account_id` as an **Integer**.
- **Error Handling:** - `400 Bad Request`: Missing account ID.
  - `404 Not Found`: Account ID has no transaction history.
  - `500 Internal Error`: Database connection or server failures.
- **Security:** Uses Environment Variables for database credentials and Parameterized SQL queries.

