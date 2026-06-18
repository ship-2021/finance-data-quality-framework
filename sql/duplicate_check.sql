SELECT
transaction_id,
COUNT(*)
FROM source_transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;