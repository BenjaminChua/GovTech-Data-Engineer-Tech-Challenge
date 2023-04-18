# Section 2: Databases

## How to use
1. Build Image
    ```
    docker build -t benjaminchua/govtech_data_eng
    ```
2. Run Image (i.e. PostgreSQL DB instance)
    ```
    docker run -it --rm -e POSTGRES_PASSWORD=mysecretpassword benjaminchua/govtech_data_eng
    ```
3. Populate Database and Query


## ER Diagram
![alt text](ER-Diagram.png "ER Diagram")

## Design
There are 4 tables namely members, items, transactions, transaction_items.
- Members can be populated by upstream validation checks and application approvals
- Items can be added by an administrator or manufacturers
- Both transaction_items and transactions need to be populated together as they are dependent. Transaction_items hold a more granular view of the transactions with each item of each transaction taking 1 row. Transactions hold a more aggregated view of transaction_items with total_price and total_weight of all the items bought in 1 transaction.
- Analysis can be done easily on the transactions or transaction_items tables but an improvement could be to have a replica of these tables or an analytics table where the analysis will not take up any resources from the operations of creating transactions 

## Analysis SQL queries
### Which are the top 10 members by spending
``` SQL
SELECT membership_id, SUM(total_price) lifetime_spending FROM transactions GROUP BY membership_id ORDER BY lifetime_spending DESC LIMIT 10;
```
### Which are the top 3 items that are frequently bought by members
_This assumes quantity rather than price or transaction count_
``` SQL
SELECT item_id, SUM(quantity) lifetime_quantity_sold FROM transaction_items GROUP BY item_id ORDER BY lifetime_quantity_sold DESC LIMIT 3;
```