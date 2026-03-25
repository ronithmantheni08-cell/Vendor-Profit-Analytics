import pandas as pd
import sqlite3
import os
import time

# 1. SETUP: Paths and file definitions
data_folder = "/Users/ronithmantheni/Documents/data"
db_path = os.path.join(data_folder, "vendor_analysis.db")

files = [
    "begin_inventory.csv", "end_inventory.csv", 
    "purchase_prices.csv", "vendor_invoice.csv",
    "Purchases.csv", "Sales.csv"
]

def run_pipeline():
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    print("--- 🚀 Phase 2: Loading Raw Data ---")

    for file in files:
        path = os.path.join(data_folder, file)
        if os.path.exists(path):
            print(f"Ingesting {file}...")
            # We use chunks to keep Mac's memory usage low
            chunks = pd.read_csv(path, chunksize=100000)
            for i, chunk in enumerate(chunks):
                # Standardize column names (no spaces, no dots)
                chunk.columns = [c.strip().replace(' ', '_').replace('.', '') for c in chunk.columns]
                mode = 'replace' if i == 0 else 'append'
                table_name = file.split('.')[0].lower()
                chunk.to_sql(table_name, conn, if_exists=mode, index=False)
            print(f"✅ {file} loaded.")

    print("\n--- 🛠️ Phase 3: SQL Transformation (The Heavy Lifting) ---")
    
    # We join Sales to Purchase Prices to get the Cost of Goods Sold (COGS).
    # NOTE: We use 'VendorNo' from Sales and 'VendorNumber' from Purchase_Prices
    sql_logic = """
    CREATE TABLE IF NOT EXISTS master_vendor_data AS
    SELECT 
        s.Brand,
        s.Description,
        s.VendorNo,
        pp.VendorName,
        SUM(s.SalesQuantity) as Total_Qty_Sold,
        SUM(s.SalesDollars) as Total_Revenue,
        pp.PurchasePrice as Unit_Cost,
        SUM(s.SalesQuantity * pp.PurchasePrice) as Total_COGS,
        (SUM(s.SalesDollars) - SUM(s.SalesQuantity * pp.PurchasePrice)) as Gross_Profit
    FROM sales s
    LEFT JOIN purchase_prices pp ON s.Brand = pp.Brand AND s.VendorNo = pp.VendorNumber
    GROUP BY s.VendorNo, s.Brand;
    """

    try:
        conn.execute(sql_logic)
        conn.commit()
        print("✅ SUCCESS: 'master_vendor_data' table created for Tableau!")
    except Exception as e:
        print(f"❌ SQL ERROR: {e}")

    conn.close()
    print(f"\n--- 🎉 PIPELINE COMPLETE: Database ready at {db_path} ---")

if __name__ == "__main__":
    run_pipeline()