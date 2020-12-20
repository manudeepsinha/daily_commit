#Connecting to a database, first make sure mysql connector is installed
#importing the sql connector for mysql
import mysql.connector as msc

mydb = msc.connect (user = 'root',
                  host = 'localhost',
                  password = 'lol')

#using cursor() to navigate through databases
cursor = mydb.cursor()

cursor.execute('CREATE DATABASE my_test_db')

#Databse named my_test_db will be created



#Following is another code for printing all databases.
#importing the sql connector for mysql
import mysql.connector as msc

mydb = msc.connect (user = 'root',
                  host = 'localhost',
                  password = 'lol')

#using cursor() to navigate through databases
cursor = mydb.cursor()

cursor.execute ('SHOW DATABASES')

for x in cursor:
    print(x)


