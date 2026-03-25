import pandas as pd
import sqlite3

# Path to your database
db_path = "/Users/ronithmantheni/Documents/data/vendor_analysis.db"
output_path = "/Users/ronithmantheni/Documents/data/tableau_master.csv"

def export():
    print("--- 🔄 Converting Database to Tableau-Friendly CSV ---")
    conn = sqlite3.connect(db_path)
    
    # Load the master table we built earlier
    df = pd.read_sql_query("SELECT * FROM master_vendor_data", conn)
    
    # Save as a clean CSV
    df.to_csv(output_path, index=False)
    
    conn.close()
    print(f"✅ SUCCESS! Open this file in Tableau: {output_path}")

if __name__ == "__main__":
    export()