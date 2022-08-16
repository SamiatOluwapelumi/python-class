import mysql.connector
mydb=mysql.connector.connect(
   host='localhost',
   user='root',
   passwd='sammy2000',
   database='testdb'
)
# print(mydb)
# to create database
my_cursor= mydb.cursor()
# my_cursor.execute('CREATE DATABASE testdb')

# to check if db exist or not
# my_cursor.execute('SHOW DATABASES')
# for db in my_cursor:  #to show my db
#    print(db[0])

# to create table
# my_cursor.execute('CREATE TABLE users (name varchar(255), email varchar(255),age int(10),user_id int PRIMARY KEY)')
# my_cursor.execute('SHOW TABLES')
# for table in my_cursor:
#        print(table[0])


# adding data into the table

tablestuff='INSERT INTO users(name,email,age,user_id) VALUES (%s,%s,%s,%s)'
record1=('samiat','sammy@gmail.com',21,1)
my_cursor.execute(tablestuff,record1)
mydb.commit()  #necesary to make d changes, if not there, nothing will b executed