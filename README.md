# PwC Banking Transactions API
This repository contains a production-ready FastAPI application designed to retrieve banking transactions from a PostgreSQL database, containerized with Docker and deployed on Google Cloud Platform.

## 🚀 Live Deployment
**API URL:** https://pwc-banking-api-984322524410.us-central1.run.app/transactions

**Interactive Documentation (Swagger):** https://pwc-banking-api-984322524410.us-central1.run.app/docs

## 🛠 Tech Stack
**Language:** Python 3.11

**Framework:** FastAPI (Asynchronous support)

**ORM:** SQLAlchemy (utilizing Parameterized Queries for SQL Injection protection)

**Infrastructure:** Google Cloud Run (Serverless)

**Database:** Google Cloud SQL (PostgreSQL)

**Containerization:** Docker

## ✅ Features & Acceptance Criteria
**Strict Validation:** Enforces account_id as a mandatory Integer.

**Enhanced Data Schema:** Includes transaction_id, account_id, amount, description, merchant, type, and transaction_date.

**Comprehensive Error Handling:**

***400 Bad Request:*** Triggered when the account_id query parameter is missing.

***422 Unprocessable Entity:*** Triggered by FastAPI when a non-integer value (e.g., text) is provided.

***404 Not Found:*** Triggered when an account ID has no associated transaction history.

***500 Internal Error:*** Covers database connection or unexpected server failures.

**Security:** - Unix Sockets: Uses secure internal networking to connect the API to Cloud SQL.

**Environment Variables:** Sensitive database credentials are kept out of the source code.

## 📂 Project Structure
**main.py:** Core API logic and endpoint definitions.

**schema.sql:** Database table creation and seed scripts.

**Dockerfile:** Container configuration for GCP deployment.

**requirements.txt:** Python library dependencies.


## 🛠 Deployment Instructions
**1. Database Setup (Cloud SQL)**
Create a PostgreSQL instance in Google Cloud SQL.

Execute the provided schema.sql to create the table and load seed data.

**2. Local Development**
Clone the repo: git clone https://github.com/jjjrivera44/pwc-banking-api.

Install dependencies: pip install -r requirements.txt.

Build the image: docker build -t pwc-banking-api ..

**3. Google Cloud Run Deployment**
Connect this GitHub repository to Cloud Run.

Under Connections, add your Cloud SQL instance.

Set the DATABASE_URL environment variable using the Unix Socket format.
