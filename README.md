Retail Sales Analytics – End-to-End ETL & Dashboard

<img width="1298" height="718" alt="Screenshot 2025-10-07 175228" src="https://github.com/user-attachments/assets/eac198cf-28a8-445f-b5f3-d394874c61d5" />

📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline and interactive dashboard for Retail Sales Analytics.

Tools Used: Python (pandas, SQLAlchemy), PostgreSQL, Power BI

Objective:

Extract raw retail sales data from PostgreSQL/CSV.

Transform & clean the dataset using Python.

Load the processed data into Power BI for visualization.

Build an industry-style interactive dashboard with KPIs & insights.

📂 Dataset

Source: Synthetic dataset generated for this project.

Size: 500 rows × 10 columns.

Columns:

OrderID, OrderDate, CustomerID, Product, Category, Quantity, UnitPrice, TotalAmount, Region, PaymentMethod

🔄 ETL Workflow
1. Extract

Data loaded from CSV → PostgreSQL → Python (pandas).

2. Transform

Performed with Python pandas:

Handled missing values (fillna, drop duplicates).

Standardized categorical values (e.g., Region names, Payment Methods).

Converted data types (OrderDate → datetime, amounts → numeric).

Created new features:

Profit = TotalAmount – (UnitPrice × Quantity × 0.8)

CustomerType (New vs Returning)

OrderCategory (High Value vs Low Value)

Added time-based features: Year, Month, Quarter, YearMonth.

3. Load

Cleaned dataset exported back to:

PostgreSQL (retail_sales_clean table)

CSV (retail_sales_clean.csv) for Power BI

