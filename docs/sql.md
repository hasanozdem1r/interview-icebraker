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