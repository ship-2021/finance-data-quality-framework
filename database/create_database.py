import sqlite3


# Create connection
connection = sqlite3.connect("../database/customer.db")




print("Database created successfully")

cursor=connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS customers
(
    CustomerID INTEGER,
    Name TEXT,
    City TEXT,
    Email TEXT
)
"""
cursor.execute(create_table_query)
connection.commit()


print("Customer table created")


connection.close()