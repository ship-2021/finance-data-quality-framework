
def test_batch_audit_status_is_success():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT PROCESS_STATUS
            FROM FINANCE_QA.AUDIT.ETL_BATCH_AUDIT
            WHERE BATCH_ID = 'B001'
        """)

        rows = cursor.fetchall()

        assert len(rows) == 1, (
            f"Expected one audit record for B001, found {len(rows)}"
        )
        assert rows[0][0] == "SUCCESS", (
            f"Expected SUCCESS status, found {rows[0][0]}"
        )
    finally:
        connection.close()

def test_batch_audit_counts_are_consistent():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT SOURCE_COUNT, TARGET_COUNT, REJECTED_COUNT
            FROM FINANCE_QA.AUDIT.ETL_BATCH_AUDIT
            WHERE BATCH_ID = 'B001'
        """)

        rows = cursor.fetchall()

        assert len(rows) == 1, (
            f"Expected one audit record for B001, found {len(rows)}"
        )

        source_count, target_count, rejected_count = rows[0]

        assert source_count == 3, f"Expected 3 source records, found {source_count}"
        assert target_count == 3, f"Expected 3 target records, found {target_count}"
        assert rejected_count == 0, (
            f"Expected 0 rejected records, found {rejected_count}"
        )
    finally:
        connection.close()

def test_batch_audit_timestamps_are_valid():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM FINANCE_QA.AUDIT.ETL_BATCH_AUDIT
            WHERE BATCH_ID = 'B001'
              AND (
                  START_TIME IS NULL
                  OR END_TIME IS NULL
                  OR END_TIME < START_TIME
              )
        """)

        invalid_count = cursor.fetchone()[0]

        assert invalid_count == 0, (
            f"Found {invalid_count} audit records with invalid timestamps"
        )
    finally:
        connection.close()

def test_rejected_record_count_is_not_negative():
    from database.snowflake_connection import get_snowflake_connection

    connection = get_snowflake_connection()

    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT COUNT(*)
            FROM FINANCE_QA.AUDIT.ETL_BATCH_AUDIT
            WHERE BATCH_ID = 'B001'
              AND (
                  REJECTED_COUNT IS NULL
                  OR REJECTED_COUNT < 0
              )
        """)

        invalid_count = cursor.fetchone()[0]

        assert invalid_count == 0, (
            f"Found {invalid_count} audit records with invalid rejected counts"
        )
    finally:
        connection.close()

