-- Record Count Validation

SELECT COUNT(*) AS source_count
FROM source_transactions;

SELECT COUNT(*) AS warehouse_count
FROM warehouse_transactions;

-- Amount Reconciliation

SELECT SUM(amount) AS source_amount
FROM source_transactions;

SELECT SUM(amount) AS warehouse_amount
FROM warehouse_transactions;