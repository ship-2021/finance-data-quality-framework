
import os
from dotenv import load_dotenv

load_dotenv()

keys = [
    "SNOWFLAKE_ACCOUNT",
    "SNOWFLAKE_USER",
    "SNOWFLAKE_PASSWORD",
    "SNOWFLAKE_WAREHOUSE",
    "SNOWFLAKE_DATABASE",
    "SNOWFLAKE_SCHEMA",
    "SNOWFLAKE_ROLE",
]

for key in keys:
    print(f"{key}: {'SET' if os.getenv(key) else 'MISSING'}")
