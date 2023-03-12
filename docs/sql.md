# SQL Interview Questions 

### 1. What is difference between SQL and MySQL ?
SQL is a standard language. SQL is the core of the relational database which is used for accessing and managing database
MySQL is a database management system and RDMS  such as SQL Server.


### 2. What are the different subsets of SQL?
* Data Definition Language (DDL) – It allows you to perform various operations on the database such as CREATE, ALTER, and DELETE objects.
* Data Manipulation Language(DML) – It allows you to access and manipulate data. It helps you to insert, update, delete and retrieve data from the database.
* Data Control Language(DCL) – It allows you to control access to the database. Example – Grant, Revoke access permissions.

### 3. What is a Primary Key ?
A **Primary Key (PK)** in SQL is a column (or collection of columns) or a set of columns that uniquely identifies each row in the table. Null values not allowed.

### 4. What are constraints ?
Constraints in SQL are used to specify the limit on the data type of the table. It can be specified while creating or altering the table statement

Example ;  NOT NULL, CHECK, DEFAULT, UNIQUE, PK, FK

### 5. What is a unique key ?
Uniquely identifies a single row in the table. Multiple values allowed per table. Null values allowed.

### 6. What is Foreign Key ?
**Foreign Key (FK)** maintains referential integrity by enforcing a link between the data in two tables. The foreign key in the child table references the primary key in the parent table.

### 7. What is an Index?
An index refers to a performance tuning method of allowing faster retrieval of records from the table. An index creates an entry for each value and hence it will be faster to retrieve data.

### 8. How many different types of index does SQL have ?
* **Unique**: This index does not allow the field to have duplicate values if the column is unique indexed. If a primary key is defined, a unique index can be applied automatically.
* **Clustered**:  This index reorders the physical order of the table and searches based on the basis of key values. Each table can only have one clustered index.
* **Non – Clustered**: Non-Clustered Index does not alter the physical order of the table and maintains a logical order of the data. Each table can have many nonclustered indexes.

### 9. What is the difference between clustered and non-clustered index in SQL ?

* Clustered index is used for easy retrieval of data from the database and its faster whereas reading from non clustered index is relatively slower.
* One table can only have one clustered index whereas it can have many non clustered index.

### 10. What is difference between DROP and TRUNCATE ?
DROP command removes a table and it cannot be rolled back from the database whereas TRUNCATE command removes all the rows from the table.

### 11. What is the main difference between ‘BETWEEN’ and ‘IN’ condition operators ?
BETWEEN operator is used to display rows based on a range of values in a row whereas the IN condition operator is used to check for values contained in a specific set of values.

### 12. What is the difference between DELETE and TRUNCATE statements ?
* **Delete** command is used to delete a row in a table. You can rollback data after using delete statement. It is a DML command. It is slower than Truncate
* **Truncate** is used to delete all the rows from a table. You cannot rollback data. It is a DDL command. It is faster than Delete

### 13. What is the difference between CHAR and VARCHAR2 datatype in SQL ?

* Char is a data type in SQL that can store characters of a *fixed length*. 
* Varchar is a datatype in SQL that holds characters of variable length. It uses dynamic memory location.

### 14. What are Entities and Relationships ?

**Entities**: A person, place, or thing in the real world about which data can be stored in a database. 

**Relationships**: Relation or links between entities that have something to do with each other.

### 15. What is the ACID property in a database ?

**Atomicity**: Atomicity refers to the transactions that are completely done or failed where transaction refers to a single logical operation of a data. It means if one part of any transaction fails, the entire transaction fails and the database state is left unchanged.

**Consistency**: Consistency ensures that the data must meet all the validation rules. In simple words,  you can say that your transaction never leaves the database without completing its state.

**Isolation**: The main goal of isolation is concurrency control.

**Durability**: Durability means that if a transaction has been committed, it will occur whatever may come in between such as power loss, crash or any sort of error.

### 16. Are NULL values same as that of zero or a blank space ?
 
 A NULL value is not at all same as that of zero or a blank space. NULL value represents a value which is unavailable, unknown, assigned or not applicable whereas a zero is a number and blank space is a character.

### 17. What is **CLAUSE** in SQL ?

SQL clause helps to limit the result set by providing a condition to the query. A clause helps to filter the rows from the entire set of records.

### 18. What is the difference between ‘HAVING’ clause and a ‘WHERE’ clause ?

HAVING clause can be used only with SELECT statement. It is usually used in a GROUP BY clause and whenever GROUP BY is not used, HAVING behaves like a WHERE clause.

Having Clause is only used with the GROUP BY function in a query whereas WHERE Clause is applied to each row before they are a part of the GROUP BY function in a query.

### 19. What is a Stored Procedure in SQL ?

A Stored Procedure is a function which consists of many SQL statements to access the database system. Several SQL statements are consolidated into a stored procedure and execute them whenever and wherever required which saves time and avoid writing code again and again.

**Pros**: can be used as a modular programming which means create once, store and call for several times whenever it is required. This supports faster execution. It also reduces network traffic and provides better security to the data.

**Cons**: The only disadvantage of Stored Procedure is that it can be executed only in the database and utilizes more memory in the database server.

Following stored procedure called sp_GetProductDetails which accepts a parameter called @ProductId of type INT. 
The stored procedure selects the details of the product from the Products table where the ProductId matches the value of @ProductId.
```
CREATE PROCEDURE sp_GetProductDetails
    @ProductId INT
AS
BEGIN
    SELECT ProductId, ProductName, Price
    FROM Products
    WHERE ProductId = @ProductId
END
```
You can then execute this stored procedure by passing a value for the @ProductId parameter:
```
EXEC sp_GetProductDetails @ProductId = 1;
```

### 20. What are joins in SQL ?

In SQL , a join is used to combine rows from two or more tables based on a related column between them. Joins are used to retrieve data that is spread across multiple tables in a database.

There are several types of joins in SQL, including:

* INNER JOIN / JOIN: Returns only the rows that have matching values in both tables.
* LEFT JOIN: Returns all the rows from the left table and the matched rows from the right table. If there is no match in the right table, NULL values are returned for those columns.
* RIGHT JOIN: Returns all the rows from the right table and the matched rows from the left table. If there is no match in the left table, NULL values are returned for those columns.
* OUTER JOIN / FULL OUTER JOIN: Returns all the rows from both tables, with NULL values for the columns that do not have a match in the other table.

![join visualization](img/sql/sql_joins.png)

```
-- INNER JOIN or just JOIN retrieves all users and likes that match each other 
-- ( where the id field in users matches a user_id in the likes table and vice versa )
SELECT users.name, likes.like FROM users JOIN likes ON users.id = likes.user_id;

-- LEFT JOIN retrieves all users and its likes if there is any else sets NULL in the like field
SELECT users.name, likes.like FROM users LEFT JOIN likes ON users.id = likes.user_id;

-- RIGHT JOIN is like LEFT JOIN but retrieves all likes with all matching users or NULL if it doesn't have any matching user
SELECT users.name, likes.like FROM users RIGHT JOIN likes ON users.id = likes.user_id;

-- OUTER JOIN or OUTER LEFT and RIGHT with UNION (MySQL don't support FULL OUTER JOIN) retrieves all users and likes and matches them 
-- and sets NULL on any like without any match on user  and same thing with user with no matching like
SELECT users.name, likes.like FROM users LEFT OUTER JOIN likes ON users.id = likes.user_id
UNION
SELECT users.name, likes.like FROM users RIGHT OUTER JOIN likes ON users.id = likes.user_id
```

### 21. What is data integrity ? 

Data integrity in SQL refers to the *accuracy*, *consistency*, and *reliability* of data stored in a database. It ensures that the data is complete, correct, and valid. In other words, data integrity ensures that the data is of high quality and can be relied upon for decision-making, analysis, and reporting.

There are different types of data integrity in SQL:

* Entity integrity: It ensures that each row in a table has a unique identifier, such as a primary key.
* Referential integrity: It ensures that the relationships between tables are maintained, and any foreign key values in one table refer to valid primary key values in another table.
* Domain integrity: It ensures that the data in each column of a table conforms to a specific set of rules, such as data type, range, and format.
* User-defined integrity: It allows users to define their own rules and constraints to ensure the accuracy and consistency of data.
* Overall, data integrity is critical for maintaining the reliability and consistency of data in a SQL database, and it helps to prevent errors, data loss, and data corruption.

### 22. What is view in SQL ?

*View* is a virtual table that is based on the result of a SELECT query. It is not a physical table, but rather a stored SELECT statement that can be used to retrieve data in a specific format.

A view is created using the CREATE VIEW statement, which defines the SELECT query used to generate the view's data. The result set of the SELECT query is then stored as a named object that can be used in other SQL statements just like a regular table.

Views are useful for several reasons:

1. They provide a simplified view of complex data. A view can be used to hide the complexity of a database schema and present a simpler view of the data that is more easily understood by users.
2. They provide a way to control access to data. Views can be used to restrict access to certain columns or rows of data, so that users only see the data they need to see.
3. They provide a way to aggregate data. Views can be used to group data together and calculate summary information, such as totals or averages, which can be used for reporting or analysis.
4. They provide a way to combine data from multiple tables. Views can be used to combine data from several tables into a single view, making it easier to work with the data.
5. Overall, views are a powerful tool in SQL that can help to simplify complex data, control access to data, and provide a flexible way to work with data from multiple tables.

### 23. What are the different types of a subquery ?

**Subquery** is a query that is nested within another query. The subquery is used to retrieve data that will be used by the outer query to filter or manipulate the results.

There are two types of subqueries:

* Single-row subquery: A single-row subquery is a subquery that returns only one row of data, which is then used by the outer query as a value in a comparison or calculation. For example, a single-row subquery can be used to find the maximum value in a column and then use that value to filter the results of the outer query.
* Multiple-row subquery: A multiple-row subquery is a subquery that returns multiple rows of data, which are then used by the outer query to filter or manipulate the results. For example, a multiple-row subquery can be used to find all the customers who have ordered a particular product and then use that information to generate a report.

```
-- Single-row subquery
SELECT *
FROM products
WHERE price = (SELECT MAX(price) FROM products);

-- Multiple-row subquery
SELECT *
FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE product_id = 123);
```

Subqueries can also be classified by where they are used in a SQL statement. There are three types of subqueries based on where they are used:

* Subquery in SELECT statement: A subquery can be used in the SELECT statement to retrieve data from another table or to perform a calculation using data from another table.

* Subquery in FROM clause: A subquery can be used in the FROM clause to create a temporary table that is used by the outer query to retrieve data.

* Subquery in WHERE clause: A subquery can be used in the WHERE clause to filter the results of the outer query based on a condition that involves data from another table.

```
-- Subquery in SELECT statement
SELECT product_name, (SELECT MAX(price) FROM products) AS max_price
FROM products;

-- Subquery in FROM clause
SELECT *
FROM (SELECT customer_id, SUM(total) as total_spent FROM orders GROUP BY customer_id) AS customer_totals
WHERE total_spent > 1000;

-- Subquery in WHERE clause 
SELECT *
FROM products
WHERE category_id = (SELECT category_id FROM categories WHERE category_name = 'Electronics');
```

### 24. What is collation in SQL ?

Collation in SQL refers to the rules used to compare and sort character data, which can affect the results of SQL queries that involve character data. It determines how characters are treated in terms of case sensitivity, accent marks, and other language-specific rules. SQL supports a wide variety of collations, and each database has a default collation that is used for all character data in the database.

### 25. What is trigger in SQL ?

*Trigger* is a type of stored procedure that is automatically executed in response to certain database events, such as insert, update, or delete operations on a table.
Triggers are commonly used in database applications to enforce data consistency and integrity, or to automate tasks that need to be performed whenever data changes. However, because triggers can have a significant impact on database performance, they should be used judiciously and only when necessary.


Here is an example of a trigger in SQL:
```
CREATE TRIGGER update_customer_orders
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE customer_orders
  SET total_order_amount = total_order_amount + NEW.total_amount
  WHERE customer_id = NEW.customer_id;
END;

```
This trigger will be executed automatically after a new row is inserted into the "orders" table. The 'NEW' keyword is used to refer to the new row being inserted, and the trigger will update the "customer_orders" table to add the total amount of the new order to the corresponding customer's total order amount.