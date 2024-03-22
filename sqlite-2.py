import sqlite3
 
connection = sqlite3.connect('hotel_data.db')
 
connection.execute("INSERT INTO hotel VALUES (1, 'cakes',800,10 )");
connection.execute("INSERT INTO hotel VALUES (2, 'biscuits',100,20 )");
connection.execute("INSERT INTO hotel VALUES (3, 'chocos',1000,30 )");
 
print("Food id and Food Name\n")
 
cursor = connection.execute("SELECT FIND,FNAME from hotel ")
 
for row in cursor:
     print(row)
