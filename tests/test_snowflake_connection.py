
from database.snowflake_connection import get_snowflake_connection


connection = get_snowflake_connection()

try:
    cursor = connection.cursor()
    try:
        cursor.execute("""
            SELECT
                CURRENT_VERSION(),
                CURRENT_DATABASE(),
                CURRENT_SCHEMA()
        """)

        result = cursor.fetchone()

        print("Snowflake connection successful!")
        print("Snowflake version:", result[0])
        print("Database:", result[1])
        print("Schema:", result[2])

    finally:
        cursor.close()
finally:
    connection.close()
