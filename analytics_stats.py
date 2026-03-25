import pandas as pd
import sqlite3
import numpy as np
from scipy import stats

# Path to the database 
db_path = "/Users/ronithmantheni/Documents/data/vendor_analysis.db"

def run_analysis():
    conn = sqlite3.connect(db_path)
    
    # Pull the Master Table we built in Phase 3
    df = pd.read_sql_query("SELECT * FROM master_vendor_data", conn)
    
    # 1. Calculate Profit Margin % (Business Metric)
    df['Margin_Pct'] = (df['Gross_Profit'] / df['Total_Revenue']) * 100
    
    # 2. Separate into two groups (High Volume vs. Low Volume)
    # We want to see if selling more actually means better margins
    avg_qty = df['Total_Qty_Sold'].mean()
    high_vol = df[df['Total_Qty_Sold'] > avg_qty]['Margin_Pct'].dropna()
    low_vol = df[df['Total_Qty_Sold'] <= avg_qty]['Margin_Pct'].dropna()
    
    # 3. The T-Test (Statistical Metric)
    t_stat, p_val = stats.ttest_ind(high_vol, low_vol)
    
    print("--- 📊 VENDOR PROFITABILITY STATS ---")
    print(f"High Volume Avg Margin: {high_vol.mean():.2f}%")
    print(f"Low Volume Avg Margin:  {low_vol.mean():.2f}%")
    print(f"P-Value: {p_val:.4f}")
    
    if p_val < 0.05:
        print("\n✅ INSIGHT: The difference is STATISTICALLY SIGNIFICANT.")
        print("This means volume directly impacts your profit margins.")
    else:
        print("\n❌ INSIGHT: No significant difference found.")

    conn.close()

if __name__ == "__main__":
    run_analysis()