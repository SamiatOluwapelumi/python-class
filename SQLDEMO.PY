import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sammy2000",
  database="testdb"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# To insert multiple rows into a table, use the executemany() method.
# The second parameter of the executemany() method is a list of tuples, containing the data you want to insert:

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val) 

# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

# Get Inserted ID
# Note: If you insert more than one row, the id of the last inserted row is returned.Note: If you insert more than one row, 
# the id of the last inserted row is returned.

# print(mycursor.lastrowid)

# select all records from customer table and display the result
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# SELECTING COLUMN

# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# FETCHONE(): WILL RETURN THE FIRST ROW OF THE RESULT

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchone()

# print(myresult)

# SELECT WITH A FILTER

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# WILDCARD CHARACTER

# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )

# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# ORDER BY
# sql = "SELECT * FROM customers ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
  # print(x)

# sql = "SELECT * FROM customers ORDER BY name DESC"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# DELETE RECORD

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

# DROP TABLE

# sql = "DROP TABLE customers"

# mycursor.execute(sql)

# Drop Only if Exist
# If the table you want to delete is already deleted, or for any other reason does not exist,
#  you can use the IF EXISTS keyword to avoid getting an error.

# sql = "DROP TABLE IF EXISTS customers"

# mycursor.execute(sql)


# Update Table
# You can update existing records in a table by using the "UPDATE" statement:

# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")


# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")


# Limit the Result
# You can limit the number of records returned from the query, by using the "LIMIT" statement:

# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# Start From Another Position

# If you want to return five records,
#  starting from the third record, you can use the "OFFSET" keyword:

# Join Two or More Tables

# You can combine rows from two or more tables, based on a related column between them,
#  by using a JOIN statement.
# Consider you have a "users" table and a "products" table:

# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)