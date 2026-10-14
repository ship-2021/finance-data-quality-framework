import sqlite3

import pandas as pd

source_df = pd.read_csv("../data/customers.csv")


connection = sqlite3.connect("../database/customer.db")


cursor = connection.cursor()


# cursor.execute(
#     "SELECT * FROM customers"
# )
#
#
# records = cursor.fetchall()
#
#
# for row in records:
#     print(row)
#
#     connection.close()


cursor.execute(
        "SELECT COUNT(*) FROM customers"
    )


source_count = len(source_df)

target_count = cursor.fetchone()[0]


connection.close()


    # Assertion
assert source_count == target_count


connection.close()