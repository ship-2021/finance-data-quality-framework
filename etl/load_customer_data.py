import pandas as pd
import sqlite3


df=pd.read_csv("../data/customers.csv")

#connection the database
connection=sqlite3.connect("../database/customer.db")

#load data frame to database

df.to_sql(
    "customers",
    connection,
    if_exists="append",
    index=False
)

print("Data loaded successfully")


connection.close()
