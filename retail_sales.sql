CREATE TABLE retail_sales (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID VARCHAR(20),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Quantity INT,
    UnitPrice NUMERIC(10,2),
    TotalAmount NUMERIC(12,2),
    Region VARCHAR(50),
    PaymentMethod VARCHAR(30)
);
select * from retail_sales;
select * from retail_sales_clean;
COPY retail_sales(OrderID, OrderDate, CustomerID, Product, Category, Quantity, UnitPrice, TotalAmount, Region, PaymentMethod)
FROM 'D:\Data Analytics\ETL\retail_sales_data.csv'
DELIMITER ','
CSV HEADER;