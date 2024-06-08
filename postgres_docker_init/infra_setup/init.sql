-- Create schema
CREATE SCHEMA IF NOT EXISTS SUPERMARKET;


-- create and populate tables
create table if not exists SUPERMARKET.SALES
(
    Invoice_ID varchar primary key,
    Branch varchar,
    City varchar,
    Customer_type varchar,
    Gender varchar,
    Product_line varchar,
    Unit_price float,
    Quantity int,
    Tax float,
    Total float,
    Date varchar,
    Time varchar,
    Payment varchar,
    cogs float,
    gross_margin_percentage float,
    gross_income float,
    Rating float
);


COPY SUPERMARKET.SALES (Invoice_ID,Branch,City,Customer_type,Gender,Product_line,Unit_price,Quantity,Tax,Total,Date,Time,Payment,cogs,gross_margin_percentage,gross_income,Rating)
FROM '/data/supermarket_sales.csv' DELIMITER ',' CSV HEADER;
