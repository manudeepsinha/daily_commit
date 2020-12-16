USE sql_store;

/* 
This query is a transaction and makes sure all the statements 
run completely and treats them as one. If any one of the query/statement
fails to run due to some crash, etc. then it'll rollback the previously 
run queries.
*/
START TRANSACTION;

INSERT INTO orders (customer_id, order_date, status)
VALUES (1, '2019-01-01', 1);

INSERT INTO order_items
VALUES (LAST_INSERT_ID(), 1,1,1);

COMMIT;