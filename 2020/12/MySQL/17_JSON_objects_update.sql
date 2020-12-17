/* Before running the query, add properties column of JSON 
data type in products table
*/
USE sql_store;
UPDATE products
-- Using JSON_SET to update and add new properties 
SET properties = JSON_SET(
	properties,
    '$.weight', 20,
    '$.year_of_made', '2020'
)
WHERE product_id = 1;
