# 📊 Vendor Profitability & Performance Analytics Suite
### 🚀 MSBA End-to-End Data Engineering & BI Project

---

## 📋 Project Overview
This project focuses on optimizing a supply chain dataset containing **33 Million units** of sales and inventory data. By transitioning from disconnected CSV files to a structured SQL environment, I performed a deep-dive analysis into vendor efficiency, identifying over **$138M in Gross Profit** and pinpointing specific "Volume Traps" where profitability was lagging.

## 🛠️ Tech Stack
* **Language:** Python 3.13
* **Libraries:** Pandas (ETL), SciPy (Statistical Testing), SQLite3 (Database Management)
* **Visualization:** Tableau Desktop (Interactive Executive Dashboard)
* **Database:** SQL (Relational Schema Engineering)

## 🏗️ Data Pipeline & Architecture
1. **Extraction & Transformation:** Developed a Python ETL pipeline to merge 6 disparate datasets (Sales, Purchases, and Inventory).
2. **Database Engineering:** Engineered a local SQLite database to handle high-volume data joins that exceed Excel’s row limits.
3. **Statistical Validation:** Conducted an **Independent T-Test** to determine if sales volume had a statistically significant impact on profit margins ($p = 0.3353$).
4. **BI Deployment:** Connected the structured SQL output to Tableau to build a "Z-Layout" Executive Dashboard.

## 📊 Key Business Insights
* **Aggregate Margin:** Achieved a consistent **30.6% Profit Margin** across the total portfolio.
* **The 80/20 Rule:** Identified that 20% of the brand descriptions drive 80% of the total gross profit via **Pareto Analysis**.
* **Concentration Risk:** Visualized vendor dominance, highlighting **Diageo North America** as the primary profit driver.

## 📈 Dashboard Features
* **KPI Scorecards:** Instant visibility into Revenue, Margin %, and Unit Scale.
* **Brand Performance Quadrant:** A scatter plot identifying "Stars" vs. "Underpriced" brands.
* **Capital Density Map:** A packed-bubble chart showing where inventory capital is currently tied up.
* **Interactive Drill-Downs:** Global filters allow executives to click a vendor and instantly update all metrics.

---
*Developed as part of my Master of Science in Business Analytics (MSBA) portfolio.*
