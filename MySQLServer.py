# A MySQL database for an online bookstore
import mysql.connector
from mysql.connector import Error

# Connect to MySQL server

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="Syd",
        password="Pass"
    )

    mycursor = mydb.cursor()
    #In case the db does not exist, create it
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    # Select the database
    mycursor.execute("USE alx_book_store")

    # Creating the table, Authors, to store author info
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INT PRIMARY KEY,
        author_name VARCHAR(215)
    )
    """)

    # Creating the table, Books, to store info about books
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT PRIMARY KEY,
        title VARCHAR(130),
        author_id INT,
        price DOUBLE,
        publication_date DATE,
        FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    )
    """)

    # Creating the table, Customers, to store customer info
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT PRIMARY KEY,
        customer_name VARCHAR(215),
        email VARCHAR(215),
        address TEXT
    )
    """)

    # Creating the table, Orders, to store orders
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    )
    """)

    # Creating the table, Order_Details, to store order details
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS Order_Details (
        order_detailid INT PRIMARY KEY,
        order_id INT,
        book_id INT,
        quantity DOUBLE,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
    """)

    print("Database and tables created successfully.")

except mysql.connector.Error:
    print(f"Error while connecting to MySQL")