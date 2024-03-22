import sqlite3
 
connection_obj = sqlite3.connect('geek.db')
 
cursor_obj = connection_obj.cursor()
 
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

table = """ CREATE TABLE GEEK (
            Email VARCHAR(255) NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Score INT
        ); """
cursor_obj.execute(table)
print("Table is Ready")
connection_obj.close()
