USE sql_store;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
/* We can use other isolation like READ COMMITTED(default)
or REPEATABLE READ to work faster but doesn't solve
PHANTOM READ problem.
*/
START TRANSACTION;
SELECT * FROM customers WHERE state = 'VA';
COMMIT;

-- NOTE, THE FOLLOWING TRANSACTION IS FOR ANOTHER INSTANCE --
-- At another instance/user, other query is being used like --

USE sql_store;
START TRANSACTION;
UPDATE customers
SET state = 'VA'
WHERE customer_id = 3;
COMMIT;

/* Here, using serializable transaction isolation will fetch
the customer_id 3 as well as it'll wait till the second transaction
gets committed.
*/