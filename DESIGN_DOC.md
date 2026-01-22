**# Technical Design & Test Summary: Banking Transactions API

## 1. Architectural Decisions
This API was designed with **Enterprise Scalability** and **Data Integrity** as the primary drivers.

* **FastAPI Framework:** Chosen for its high performance (Asynchronous support) and native OpenAPI/Swagger integration, which reduces time-to-market for frontend teams.
* **PostgreSQL:** Selected as the relational engine to ensure **ACID compliance**, which is non-negotiable for banking transaction accuracy.
* **Serverless Framework:** Deployed via Google Cloud Run using Docker. This allows the API to scale from zero to multiple instances automatically based on demand, ensuring cost-efficiency and performance.
* **Separation of Concerns:** The application logic is decoupled from the data layer, allowing for independent scaling of the database and the API service.

## 2. Security Posture
In a banking context, security is integrated into the design rather than added as an afterthought:

* **SQL Injection Protection:** All database queries utilize **Bind Parameters** (Parameterized Queries). This ensures that user input is never executed as code.
* **Credential Security:** Database connection strings are managed via **Environment Variables**. No sensitive credentials exist in the source code or version history.
* **Encrypted Transit:** The API is served over **HTTPS (TLS/SSL)** to protect sensitive financial data while in transit.

## 3. Data Schema Enhancements
To support modern banking features, the schema was refined to include:
- `transaction_id`: A unique, auto-incrementing integer (Primary Key) for auditing.
- `merchant`: A dedicated field for transaction categorization.
- `transaction_type`: Explicitly labels "debit" vs "credit" for financial reconciliation.

## 4. Test Execution Report
I performed **Edge Case Testing** to ensure the API handles failures gracefully.

| Test Scenario | Input (`account_id`) | Expected HTTP Status | Outcome |
| :--- | :--- | :--- | :--- |
| **Successful Retrieval** | `123` | 200 OK | ✅ Passed |
| **Missing Parameter** | (Empty) | 400 Bad Request | ✅ Passed |
| **Non-Existent Account**| `999` | 404 Not Found | ✅ Passed |
| **Invalid Data Type** | `abc` | 422 Unprocessable | ✅ Passed |
| **Database Downtime** | (Simulated) | 500 Internal Error | ✅ Passed |

---
**Prepared by:** Jessie John J. Rivera

**Role:** Candidate

**
