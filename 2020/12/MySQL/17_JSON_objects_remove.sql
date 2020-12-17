/* Before running the query, add properties column of JSON 
data type in products table
*/
USE sql_store;
UPDATE products
-- Using JSON_REMOVE to remove the properties 
SET properties = JSON_REMOVE(
	properties,
    '$.year_of_made'
)
WHERE product_id = 1;
