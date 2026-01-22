-- ---SCHEMA SETUP --- --

DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    merchant VARCHAR(255), -- New column for Merchant name
    description VARCHAR(255),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    type VARCHAR(50) NOT NULL
);

-- --- UPDATED SEED DATA ---
INSERT INTO transactions (account_id, amount, merchant, description, date, type)
VALUES 
(123, -45.50, 'Starbucks', 'Morning coffee', '2026-01-22 10:38:48.332', 'debit'),
(123, 2500.00, 'PwC', 'Monthly Salary', '2026-01-22 10:38:48.332', 'credit'),
(123, -120.00, 'Shell', 'Fuel', '2026-01-22 10:38:48.332', 'debit'),
(456, -15.99, 'Netflix', 'Subscription', '2026-01-22 10:38:48.332', 'debit'),
(456, 500.00, 'Family', 'Birthday Gift', '2026-01-22 10:38:48.332', 'credit'),
(123, -200.00, 'SM Supermarket', 'Groceries', '2026-01-22 10:38:48.332', 'debit'),
(123, -45.50, 'Starbucks', 'Morning coffee', '2026-01-22 10:39:41.952', 'debit'),
(123, 2500.00, 'PwC', 'Monthly Salary', '2026-01-22 10:39:41.952', 'credit'),
(456, -120.00, 'Shell', 'Fuel', '2026-01-22 10:39:41.952', 'debit'),
(456, -15.99, 'Netflix', 'Subscription', '2026-01-22 10:39:41.952', 'debit'),
(456, 500.00, 'Family', 'Birthday Gift', '2026-01-22 10:39:41.952', 'credit'),
(456, -200.00, 'SM Supermarket', 'Groceries', '2026-01-22 10:39:41.952', 'debit');