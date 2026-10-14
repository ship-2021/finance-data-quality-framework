from database.snowflake_connection import get_snowflake_connection


def test_no_invalid_quantities():
    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM FINANCE_QA.CURATED.CURATED_TRADES
                WHERE QUANTITY IS NULL
                   OR QUANTITY <= 0
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} trades with invalid quantities"
            )
        finally:
            cursor.close()
    finally:
        connection.close()


def test_no_invalid_prices():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM FINANCE_QA.CURATED.CURATED_TRADES
                WHERE PRICE IS NULL
                   OR PRICE < 0
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} trades with invalid prices"
            )
        finally:
            cursor.close()
    finally:
        connection.close()

def test_no_invalid_currencies():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM FINANCE_QA.CURATED.CURATED_TRADES
                WHERE CURRENCY IS NULL
                   OR CURRENCY NOT IN ('USD', 'EUR', 'GBP')
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} trades with invalid currencies"
            )
        finally:
            cursor.close()
    finally:
        connection.close()

def test_required_trade_fields_present():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM FINANCE_QA.CURATED.CURATED_TRADES
                WHERE TRADE_ID IS NULL
                   OR ORDER_ID IS NULL
                   OR INSTRUMENT_ID IS NULL
                   OR TRADE_STATUS IS NULL
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} trades with missing required fields"
            )
        finally:
            cursor.close()
    finally:
        connection.close()

