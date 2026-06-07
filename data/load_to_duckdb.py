import duckdb
import pandas as pd

con = duckdb.connect('data/vendor_pricing.duckdb')

con.execute("""
    CREATE TABLE IF NOT EXISTS raw_vendors AS 
    SELECT * FROM read_csv_auto('data/raw/vendors.csv')
""")

con.execute("""
    CREATE TABLE IF NOT EXISTS raw_orders AS 
    SELECT * FROM read_csv_auto('data/raw/orders.csv')
""")

print("✅ Tables created:")
print(con.execute("SHOW TABLES").fetchdf())
print("\n📊 Vendors sample:")
print(con.execute("SELECT * FROM raw_vendors LIMIT 3").fetchdf())
print("\n📊 Orders sample:")
print(con.execute("SELECT * FROM raw_orders LIMIT 3").fetchdf())

con.close()
