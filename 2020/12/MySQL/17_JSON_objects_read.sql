/* Before running the query, add properties column of JSON 
data type in products table
*/
USE sql_store;
UPDATE products
-- Using internal functions of MySQL
SET properties = JSON_OBJECT(
	'weight',10,
    'dimensions', JSON_ARRAY(1,2,3),
    'manufacturer', JSON_OBJECT('name','sony')
)
/* Another approach that's standard among other databases
is as follows:
'
{
	"dimensions": [1,2,3],
    "weight": 10,
    "manufacturer": { "name": "sony" }
}
'
*/
WHERE product_id = 1;


-- NOTE, THE FOLLOWING QUERY IS FOR ANOTHER SCRIPT TO ACCESS THE JSON INPUTS--

SELECT 
	product_id, 
	properties -> '$.weight' AS weight,
    properties -> '$.dimensions[1]' AS '2nd_dimension',
    properties ->> '$.manufacturer.name' AS manufacturer
-- Another way JSON_EXTRACT (properties, '$.weight') AS weight
FROM products
WHERE product_id = 1;