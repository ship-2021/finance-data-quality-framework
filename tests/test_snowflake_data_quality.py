
from database.snowflake_connection import get_snowflake_connection


def test_curated_trades_count():
    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT COUNT(*) FROM FINANCE_QA.CURATED.CURATED_TRADES"
            )
            result = cursor.fetchone()

            assert result[0] == 3, (
                f"Expected 3 curated trades, but found {result[0]}"
            )
        finally:
            cursor.close()
    finally:
        connection.close()
def test_no_missing_trades():
    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM FINANCE_QA.RAW.RAW_TRADES r
                LEFT JOIN FINANCE_QA.CURATED.CURATED_TRADES c
                    ON r.TRADE_ID = c.TRADE_ID
                    AND r.BATCH_ID = c.BATCH_ID
                WHERE c.TRADE_ID IS NULL
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} raw trades missing from curated data"
            )
        finally:
            cursor.close()
    finally:
        connection.close()

def test_no_duplicate_trades():
    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM (
                    SELECT TRADE_ID, BATCH_ID
                    FROM FINANCE_QA.CURATED.CURATED_TRADES
                    GROUP BY TRADE_ID, BATCH_ID
                    HAVING COUNT(*) > 1
                ) duplicates
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} duplicate trade groups"
            )
        finally:
            cursor.close()
    finally:
        connection.close()

def test_trade_prices_match():
    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM FINANCE_QA.RAW.RAW_TRADES r
                JOIN FINANCE_QA.CURATED.CURATED_TRADES c
                    ON r.TRADE_ID = c.TRADE_ID
                    AND r.BATCH_ID = c.BATCH_ID
                WHERE r.PRICE != c.PRICE
                   OR (r.PRICE IS NULL AND c.PRICE IS NOT NULL)
                   OR (r.PRICE IS NOT NULL AND c.PRICE IS NULL)
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} trades with mismatched prices"
            )
        finally:
            cursor.close()
    finally:
        connection.close()
