/* Always a good practice to write IF NOT EXISTS before creating new tables/databases */
CREATE DATABASE IF NOT EXISTS sql_store_practice;

USE sql_store_practice;

/* When executing again, if drop customers table first, it won't work as customers table is used in orders table */
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE IF NOT EXISTS customers
(
	/* Not adding last_name column. It'll be added using ALTER TABLE*/
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name  VARCHAR(50) NOT NULL,
    points      INT NOT NULL DEFAULT 0,
    email       VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS orders
(
	order_id INT PRIMARY KEY,
    customer_id  INT NOT NULL,
    /* Standard convention is to write fk followed by child's table followed by parent's table and then column name of child's table in braces */
    FOREIGN KEY fk_orders_customers (customer_id) 
    /* Now references are added -> parent's table followed by column name in parent's table in braces*/
		REFERENCES customers (customer_id)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);