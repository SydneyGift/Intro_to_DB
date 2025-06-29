#A MySQL database for an online bookstore
import mysql.connector

#Creating the database alx bok store
alx_book_store = mysql.connector.connect(
    host = "localhost",
    user = "Syd",
    password = "Pass",
    database = "alx_book_store"
)

mycursor = alx_book_store.cursor()

#Creating the table, books, to store info about books available in the bookstore.

mycursor.execute("""
CREATE TABLE Books(
    book_id PRIMARY KEY,
    title VARCHAR(130)
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    price DOUBLE
    publication_date DATE
)
                 """)

#Creating the table, Authors, to store author info.
mycursor.execute("""
CREATE TABLE Authors(
    author_id PRIMARY KEY,
    author_name VARCHAR(215)
)
                 """)

#Creating the table, Customers, to store customer info.
mycursor.execute("""
CREATE TABLE Customers(
    customer_id PRIMARY KEY,
    customer_name VARCHAR(215)
    email VARCHAR(215)
    address TEXT
)
                 """)

#Creating the table, Orders, to store info about orders placed by customers.
mycursor.execute("""
CREATE TABLE Orders(
    order_id PRIMARY KEY,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    order_date DATE
)
                 """)

#Creating the table, Order_Details, to store info about books included in each order placed by customers.
mycursor.execute("""
CREATE TABLE Order_Details(
    order_detailid PRIMARY KEY,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
    quantity DOUBLE
)
                 """)