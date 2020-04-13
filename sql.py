#!/usr/bin/python
#coding=utf-8

import sqlite3

# !SQLite接口教程
# !https://www.runoob.com/sqlite/sqlite-python.html
class mDatabase():
      def __init__(self):
            self.conn = sqlite3.connect('movie_info.db')
            c = conn.cursor()
            print("Opened database successfully")
            c.execute('''CREATE TABLE COMPANY
                        (ID INT PRIMARY KEY     NOT NULL,
                        NAME           TEXT    NOT NULL,
                        AGE            INT     NOT NULL,
                        ADDRESS        CHAR(50),
                        SALARY         REAL);''')
            print("Table created successfully")
            conn.commit()
            conn.close()
      
      def Insertdata(self):
      c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (1, 'Paul', 32, 'California', 20000.00 )")

      c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

      c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

      c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

      conn.commit()
      print("Records created successfully")
      conn.close()
