import pandas as pd

#location of our source
file_path= "../data/customers.csv"

df= pd.read_csv(file_path)

print(df)

record_count=len(df)
print("Total Records:", record_count)
if record_count > 1:
    print("file have record ")
else:
    print("no data")

#column Validation

expected_col=["CustomerID","Name","City","Email"]
if list(df.columns)==expected_col:
    print("col validation sucessfully")
else:
    print("missing col")

    print(df.isnull().sum())
duplicate_count = df["CustomerID"].duplicated().sum()
duplicate_columns = df.columns.duplicated().sum()

print("Duplicate columns:", duplicate_columns)
print("Duplicate Customers:", duplicate_count)