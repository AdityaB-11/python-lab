# Import module 
import sqlite3
conn = sqlite3.connect('geeks2.db') 
  
cursor = conn.cursor() 
  
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), 
SECTION VARCHAR(255));"""
cursor.execute(table) 
  
cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')''') 
  
print("Data Inserted in the table: ") 
data=cursor.execute('''SELECT * FROM STUDENT''') 
for row in data: 
    print(row) 
       
conn.commit() 
conn.close()
