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
