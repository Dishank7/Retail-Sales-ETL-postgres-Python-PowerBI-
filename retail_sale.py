import pandas as pd
from sqlalchemy import create_engine


username = "postgres"
password = "D.clown.7"
host = "localhost"
port = "5432"
database = "ETL"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

sales_data = pd.read_sql("select * from retail_sales",engine)
# print(sales_data)

# Cleaning & transforming data
sales_data.dropna(inplace=True)
sales_data = sales_data.drop_duplicates(subset=["orderid"])
sales_data["region"].fillna("Unknown",inplace=True)
sales_data["paymentmethod"].fillna("Other",inplace=True)


# Standardize category
sales_data["region"]=sales_data["region"].str.strip().str.title()
sales_data["paymentmethod"]=sales_data["paymentmethod"].replace({
    "CC":"Credit Card",
    "CreditCard":"Credit Card",
    "Cash On Delivery":"COD"
})

# Convert Data types
sales_data["orderdate"] = pd.to_datetime(sales_data["orderdate"])
sales_data["quantity"] = pd.to_numeric(sales_data["quantity"])
sales_data["unitprice"] = pd.to_numeric(sales_data["unitprice"])
sales_data["totalamount"] = pd.to_numeric(sales_data["totalamount"])


# Adding Column
sales_data["year"] = sales_data["orderdate"].dt.year
sales_data["month"] = sales_data["orderdate"].dt.month
sales_data["quarter"] = sales_data["orderdate"].dt.quarter
sales_data["profit"] = sales_data["totalamount"]-(sales_data["unitprice"]*sales_data["quantity"]*0.8)
sales_data["ordercategory"] = sales_data["totalamount"].apply(lambda x :"high value" if x > 500 else "low value")


# customer insight
sales_data =  sales_data.sort_values(["customerid","orderdate"])
sales_data["customertype"] = sales_data.groupby("customerid").cumcount().apply(lambda x : "New" if x == 0 else "Returning")

# print("done")

# sales_data.to_sql("retail_sales_clean",engine,if_exists="replace",index=False)

# sales_data.to_csv("retail_sale_clean.csv",index=False)






