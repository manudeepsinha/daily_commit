USE sql_store_practice;
/* Modifying defined databases/tables is done using ALTER. It can add, modify, and delete columns */
ALTER TABLE customers
	ADD last_name     VARCHAR(50) NOT NULL AFTER first_name,
    MODIFY first_name VARCHAR(55) DEFAULT '',
    DROP points;