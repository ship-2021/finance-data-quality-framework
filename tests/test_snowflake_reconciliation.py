from database.snowflake_connection import get_snowflake_connection


def test_raw_and_curated_totals_match():
    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT
                    COUNT(*) AS TRADE_COUNT,
                    SUM(QUANTITY) AS TOTAL_QUANTITY,
                    SUM(QUANTITY * PRICE) AS TOTAL_TRADE_VALUE
                FROM FINANCE_QA.RAW.RAW_TRADES
                WHERE BATCH_ID = 'B001'
            """)
            raw = cursor.fetchone()

            cursor.execute("""
                SELECT
                    COUNT(*) AS TRADE_COUNT,
                    SUM(QUANTITY) AS TOTAL_QUANTITY,
                    SUM(QUANTITY * PRICE) AS TOTAL_TRADE_VALUE
                FROM FINANCE_QA.CURATED.CURATED_TRADES
                WHERE BATCH_ID = 'B001'
            """)
            curated = cursor.fetchone()

            assert raw == curated, (
                f"Raw totals {raw} do not match curated totals {curated}"
            )
        finally:
            cursor.close()
    finally:
        connection.close()


def test_trade_level_values_match():
    from database.snowflake_connection import get_snowflake_connection

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
                WHERE r.BATCH_ID = 'B001'
                  AND (
                      r.QUANTITY != c.QUANTITY
                      OR (r.QUANTITY IS NULL AND c.QUANTITY IS NOT NULL)
                      OR (r.QUANTITY IS NOT NULL AND c.QUANTITY IS NULL)
                      OR r.PRICE != c.PRICE
                      OR (r.PRICE IS NULL AND c.PRICE IS NOT NULL)
                      OR (r.PRICE IS NOT NULL AND c.PRICE IS NULL)
                  )
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} trades with quantity or price mismatches"
            )
        finally:
            cursor.close()
    finally:
        connection.close()

def test_no_extra_curated_trades():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        try:
            cursor.execute("""
                SELECT COUNT(*)
                FROM FINANCE_QA.CURATED.CURATED_TRADES c
                LEFT JOIN FINANCE_QA.RAW.RAW_TRADES r
                    ON c.TRADE_ID = r.TRADE_ID
                    AND c.BATCH_ID = r.BATCH_ID
                WHERE c.BATCH_ID = 'B001'
                  AND r.TRADE_ID IS NULL
            """)

            result = cursor.fetchone()

            assert result[0] == 0, (
                f"Found {result[0]} curated trades missing from raw data"
            )
        finally:
            cursor.close()
    finally:
        connection.close()

def test_batch_trade_counts_match():
    global cursor
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        query = """
            SELECT
                (SELECT COUNT(*)
                 FROM FINANCE_QA.RAW.RAW_TRADES
                 WHERE BATCH_ID = 'B001') AS RAW_COUNT,
                (SELECT COUNT(*)
                 FROM FINANCE_QA.CURATED.CURATED_TRADES
                 WHERE BATCH_ID = 'B001') AS CURATED_COUNT
        """
        cursor.execute(query)
        raw_count, curated_count = cursor.fetchone()

        assert raw_count == curated_count, (
            f"Batch B001 count mismatch: "
            f"RAW={raw_count}, CURATED={curated_count}"
        )
    finally:
        cursor.close()

def test_raw_trades_have_valid_batch_ids():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM FINANCE_QA.RAW.RAW_TRADES
            WHERE BATCH_ID IS NULL
               OR TRIM(BATCH_ID) = ''
        """)

        invalid_count = cursor.fetchone()[0]

        assert invalid_count == 0, (
            f"Found {invalid_count} RAW trades with missing batch IDs"
        )
    finally:
        connection.close()

def test_raw_trades_have_event_timestamps():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM FINANCE_QA.RAW.RAW_TRADES
            WHERE EVENT_TIME IS NULL
        """)

        invalid_count = cursor.fetchone()[0]

        assert invalid_count == 0, (
            f"Found {invalid_count} RAW trades with missing event timestamps"
        )
    finally:
        connection.close()

