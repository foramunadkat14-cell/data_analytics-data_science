# What is SQL?
    SQL (Structured Query Language) is a standard language used to manage and query relational databases. It allows you to create, read, update, and delete data as well as define and manage database schemas and relationships between tables.

**Key points:**

1. SQL is a structured query language for interacting with relational databases.
2. It is used to create databases and tables and to define schemas.
3. SQL manages relationships between tables using keys and constraints.
4. Basic SQL operations include SELECT, INSERT, UPDATE, DELETE, CREATE, and DROP.
5. SQL keywords are generally case-insensitive, though identifiers and behavior can vary by implementation

# Advantages of SQL:
1. Powerful querying: supports complex queries, filtering, aggregation, and joins.
2. Standardized: widely adopted ANSI/ISO standard with consistent core syntax.
3. Mature tooling: extensive ecosystem of database engines, clients, and administration tools.
4. Data integrity: supports constraints, transactions, and ACID properties in many systems.
5. Scalability and performance: optimized engines and indexing for large datasets.
6. Declarative: you specify what you want, and the database engine decides how to execute it.



# SQL  commands or query 
1. SQL provides some query or commands
2. SQL is case - insenstive 
    examples: INSERT | insert | Insert
3. best way to write query in small case


**types of SQL query**

1. DDL (data definition language)
2. DML (data manipulation language)
3. DQL (data query language)
4. TCL ( transactional query language)

# mysql start database

1. xampp is server tools
    X - cross plateform(support all OS)
    A - apache (server)
    M - MySQL (database)
    P - perl
    P - php

2. mysql workbench2.0

    MySQL wrokbench is also used for mysql database
    MySQL workbench is also used to create database | tables create

# DDL (Data Definition Language)

1. DDL is used to create a database and table strucutred
2. DDL is also used to add | modify | rename any coloumn name of table.
3. DDL also drop and truncate a structure
4. DDL is also used to change the coloumn of table 

**examples of DDL**

1. create
2. alter
3. rename
4. drop
5. change
6. truncate

**How to create a database structured**

**syntax**

'''

create database databasename;
or 
create database flipkart_shop;

'''

**how to create a table structures**

**chart of tables to create fieldname and datatype and its size in sql**


| Field Name    | Data Type      | Size      | Description              |
|---------------|----------------|-----------|--------------------------|
| emp_id        | INT            | 11        | Employee ID (Primary Key)|
| first_name    | VARCHAR        | 50        | Employee First Name      |
| last_name     | VARCHAR        | 50        | Employee Last Name       |
| gender        | VARCHAR        | 10        | Gender                   |
| email         | VARCHAR        | 100       | Email Address            |
| phone         | BIGINT         | 10        | Mobile Number            |
| department    | VARCHAR        | 50        | Department Name          |
| salary        | DECIMAL        | 10,2      | Employee Salary          |
| hire_date     | DATE           | —         | Joining Date             |
| city          | VARCHAR        | 50        | City Name                |



**syntax to create a table in sql**

'''
  
create table tablename
(
    columnname1 datatype(size) auto_increment ,
    coulmnname2 datatype(size),
)


'''

**example**

'''

create table employee
(
    empid int primary key AUTO_INCREMENT,
    name varchar(155),
    password varchar(255),
    email varchar(255),
    phone bigint,
    address text

);

'''

'''

create table contact
(
    contactid int primary key AUTO_INCREMENT,
    name varchar(155),
    email varchar(255),
    subject ENUM ('24x7 customer support','return produts','customer care numbers'),
    phone bigint,
    message text

);

'''

'''

create table review
(
    reviewid int primary key AUTO_INCREMENT,
    name varchar(155),
    email varchar(255),
    phone bigint,
    ratings ENUM('1 star' , '2 star' , '3 star' , '4 star' , '5 star'),
    comment text
);

'''

'''

CREATE TABLE products 
(
    product_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT(11),
    description TEXT,
    manufacture_date DATE,
    expiry_date DATE,
    weight DECIMAL(6,2),
    color VARCHAR(30),
    size VARCHAR(20),
    supplier_name VARCHAR(100),
    rating DECIMAL(3,1),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

'''


# alter

'''
    alter is use to add , modify, update , drop a column from tables

    1. alter table employee add added_date date;
    2. alter table employee add is_active boolean DEFAULT TRUE;
    3. alter table employee add photo blob after email;
    4. alter table employee CHANGE name employeename varchar(255)
    5. alter table employee drop photo;
'''


# rename : after create tables we rename the table name

'''
    rename table table_name to updated_name
'''

# drop: drop is drop database and table both after drop we can not rollback anything

'''

drop database databasename;
or 
drop table tablename;
'''


# truncate : 

    1. truncate is use to dlt data only from tables
    2. truncate is also use to empty tables rows
    3. after truncate data from tables we can not rollback data

    '''
        truncate table tablename;

    '''

# DML: data manipulation language

    1. DML is use to manipulate data in tables
    2. DML is use to insert | delete | update data in tables. 


**insert data in tables**

1. syntax 

```
    inster into tablename(col1,col2,col3) values('val1', 'val2', 'val3')
```

**delete data in tables**

    1. delete is use to delete all data from tables
    2. delete is use to delete particular data from tables
    3. delete is use to delete alternate data from tables
    4. delete is use to delete a range of data from tables
    5. after delete we rollback our data

**syntax** 

```
    1.  delete all data from table 

        delete from tablename

    2. delete perticular one data

        delete from tablename where id=5;
        or
        delete from tablename  where name=riya;

    3. delete alternate data from tables

        delete from tablename where id in(1,3)
        
    4. delete range of data from tables

        delete from tablename where id between 51 and 100;

```


**update  data in tables**

    1. update any rows or data from tables

**syntax**

```
update tablename set col1='value1',col2='value2', col3='value3', where id=2;
```

# DQL : data query language
 
    1. DQL is use to fetch data or select data from tables
    2. DQL is use to fetch all data  | particular data | alternate data | range data | limit of data.
    3. DQL is use "select"

3. select particular column name data 

4. select range of data from tables

``` 
select * from tablename where id between 5 and 10;
```

5. select alternate data from tables

``` 
select * from tablename where id in(12,15,13);
```
 
**order by and group by**

# order by :

    1. order by filter data from tables in acending order or decending order 
    2. order by is used to sort data in acending or decending order.

**syntax**

```
select * from tablename order by columnname asc;
or
select * from tablename order by columnname desc;

examples: 

select * from flip_reviews order by name asc;
or
select * from flip_reviews order by name dasc;
```

SQL function :

1. SQL function is used to perform some operations on data and return a single value
2. SQL function is used to perform some operations on data and return a single value

# types of SQL function

1. aggregate function

   1. sum(): returns the total sum of a numeric column

      examples : select sum(salary) from flip_employee;
                 or
                 select sum(salary) as sumofsalary_ofemployee from flip_employee;  

  **as is used to give alias name to columnname or table name**

   2. avg(): returns the average value of a numeric column

      examples : select avg(salary) from flip_employee;
                 or
                 select avg(salary) as avgsalary_ofemployee from flip_employee;

   3. count(): returns the number of rows that match a specified condition

      examples : select count(*) from flip_employee;
                 or
                 select count(*) as totalemployee from flip_employee;
                 or
                 select count(salary) from flip_employee where salary>16000;

   4. max(): returns the maximum value of a column
      examples : select max(salary) from flip_employee;
                 or
                 select max(salary) as maxsalary_ofemployee from flip_employee;
    
   5. min(): returns the minimum value of a column

      examples : select min(salary) from flip_employee;
                 or
                 select min(salary) as minsalary_ofemployee from flip_employee;


  **note : aggregate function is used to perform some operations on data and return a single value**



2. scalar function


   1. firstname() : returns the first name of a person
   2. lastname() : returns the last name of a person
   3. length() : returns the length of a string
   4. upper() : returns the string in uppercase
   5. lower() : returns the string in lowercase
   6. round() : rounds a numeric field to the number of decimals specified
   7. now() : returns the current date and time

examples : select firstname(employeename) from flip_employee;
             or
             select lastname(employeename) from flip_employee;
             or
             select length(employeename) from flip_employee;
             or
             select ucase(name) from flip_employee;
             or
             select lcase(emplyeename) from flip_employee;
             or
             select round(salary,2) from flip_employee;
             or
             select now() from dual;

  **note : scalar function is used to perform some operations on data and return a single value**

  firstname() and lastname() function is used to return the first name and last name of a person from a full name column not supported in mysql but supported in sql server and oracle database

# group by 

 1. group by is used to group data based on a column
 2. group by is used to group data based on a column and perform aggregate functions like

  - count
  - sum
  - avg
  - max
  - min

  **syntax**
  
  ```
   select sum(salary) from flip_employee group by department;
   or
   select department, sum(salary) from flip_employee group by department;
   or
   select sum(salary),department from flip_employee GROUP by department;
   or
   select sum(salary) as totalsalary,department from flip_employee GROUP by department;

  ```

 # w.a.q to find second highest salary from employee table


**sub query**

1. query within another query is called subquery
2. subquery is used to find second highest salary from employe table

```
select salary from flip_employee order by salary dasc limit 1,1;
or
select max (salary) from flip_employee where salary < (select mac(salary) from flip_employee);
```


# like operator

1. like operator is use to search for a specified pattern in a column
2. like operator is use to search for a specified pattern in a cloumn using wildcards

** wild cards**

1. %    : represents zero or more characters
2. _    : represents a single character
3. [ ]  : represents any single character within the brackets
4. [^]  : represents any single character not within the brackets
5. -    : represents a range of charcters
6. |    : represents an  OR condition
7. \    : escape charcter
8. ^    :  represents the start of a string
9. $    : represents the end of string
10. ()  : group of a series of conditions


**syntax**
  
  ```
  select * from tablename where columnname like 'pattern';
  or
  select * from flip_employee where employeename like 'a%'
  or
  select * from flip_employee where employeename like '%v'
  or
  select * from flip_employee where employeename like '%a%'
  or
  select * from flip_employee where employeename like '_a%'
  or
  select * from flip_employee where employeename like 'a_%';
  or
  select * from flip_employee where employeename like 'a__%';
  or
  select * from flip_employee where employeename like '%bri%'
  or
  select * from flip_employee where employeename like '%or%'
  
  ```

 # key constraints in SQL ......

   1. key constraints are used to provide a limitation on a  tables 
   2. key constraints are ...

      1. primary key 
      2. unique key 
      3. foreign key  

# primary key :
 
  1. A pk key never return a null values 
  2. A pk key always have an auto_increments 
  3. A pk will provides only one times in tables
  4. A pk stored a unique values 

**create table with pk**

  ```
create table reviews
(
reviewsid int primary key AUTO_INCREMENT,
name varchar(155),
email varchar(255),
ratings ENUM('1 star','2 star','3 star','4 star','5 star'),
phone bigint,
comment text    
    
 );

```

**create in md formate**

# Reviews Table Structure

| Column Name | Data Type | Size / Values | Constraints |
|------------|-----------|---------------|-------------|
| reviewsid | INT | - | PRIMARY KEY, AUTO_INCREMENT |
| name | VARCHAR | 155 | NULL Allowed |
| email | VARCHAR | 255 | NULL Allowed |
| ratings | ENUM | '1 star', '2 star', '3 star', '4 star', '5 star' | NULL Allowed |
| phone | BIGINT | - | NULL Allowed |
| comment | TEXT | Large Text | NULL Allowed |


# unique key :
 
  1. A uk key return one times a null value   
  2. A uk will provides many times in a tables on columns
  3. A uk stored a unique values
  4. A uk never stored an dublicate values in tables 
  
**create table with uk**

  ```
ALTER TABLE `flip_register` ADD UNIQUE(`email`);
or
ALTER TABLE `flip_register` ADD UNIQUE(`phone`);
```
  
**note : here email and phone are unique key set and it is never stored a dublicate values**  

# foreign key :
    
  1. A fk will provides many times in a tables on columns with common field or column
  3. A fk are used to provides an relationship b/w one table to another table
  4. A fk can stored an dublicate key with common field

**create table with fk**

# create a flip_country table

```
create table flip_country
(
cid int AUTO_INCREMENT primary key,
countryname varchar(255)    
)
 ```

# create a flip_users table 

```
create table flip_users
(
uid int AUTO_INCREMENT primary key,
name varchar(255),
email varchar(255),
phone bigint,
cid int REFERENCES flip_country(cid)    
)

```
# create an tables with foreign key ....

# ecommerce managements

# create an database flipkart_shop

1. flip_category
2. flip_subcategory
3. flip_products 
4. flip_customers
5. flip_cart
6. flip_orders

# examples:
```
1. create database flipkart_shop
2.create table flip_category
(
 catid int AUTO_INCREMENT primary key,
 categoryname varchar(255)   
)
3.create table flip_subcategory
(
 pid int AUTO_INCREMENT primary key,   
 catid int REFERENCES flip_category(catid),
 subcategoryname varchar(255)
) 
4.create table flip_products
(
 pid int AUTO_INCREMENT primary key,   
 catid int REFERENCES flip_category(catid),
 subcatid int REFERENCES flip_subcategory(subcatid),
 pname varchar(255),
 qty int,
 oldprice int,
 photo blob,   
 offerprice int,
 descriptions text   
)  

5. create table flip_customers
(
custid int primary key AUTO_INCREMENT,
name varchar(255),
email varchar(255),
password varchar(255),
address text,
phone bigint    

)

6. create email as unique key 

alter table flip_customers add unique(`email`)

7. create table flip_cart
(
cartid int AUTO_INCREMENT primary key,
pid int REFERENCES flip_products(pid),
custid int REFERENCES flip_customers(custid),
qty int, 
price int, 
suntotal int, 
added_date varchar(255)    

)


```

# students managements  systems

1. courses
2. faculty
3. students

# task managements 

1. flip_priority
3. flip_employee 
2. flip_task


# ecommerce related tables normalisations ...

1. create table categories
(
catid int AUTO_INCREMENT primary key,
catname varchar(255)
)

2. create table subcategories
(
subcatid int AUTO_INCREMENT primary key,
subcatname varchar(255)
)

3. create table flip_products
(
 pid int AUTO_INCREMENT primary key,   
 catid int REFERENCES flip_category(catid),
 subcatid int REFERENCES flip_subcategory(subcatid),
 pname varchar(255),
 qty int,
 oldprice int,
 photo blob,   
 offerprice int,
 descriptions text   
) 


# students managements systems database normalisations 

1. priority
2. employee
3. task 


# SQL join .....

  join ...

  # join is used to join more than once table with common field if data matched from one table to another table its join 


   1. join 


    ```
    select products.*,catname,subcatname from products join categories on products.catid=categories.catid join subcategories on products.subcatid=subcategories.subcatid;
    or

    select pid, photo,pname, offerprice, descriptions, added_date_time, catname,subcatname from products join categories on products.catid=categories.catid join subcategories on products.subcatid=subcategories.subcatid;
    or

    select task.*, pname,name from task join priority on task.prid=priority.prid join employee on task.empid=employee.empid


    or

    select taskid, title, added_date,pname,name from task join priority on task.prid=priority.prid join employee on task.empid=employee.empid 
  
    ```
 
# students managements  systems

1.create table course
(
courseid int AUTO_INCREMENT primary key,
coursename varchar(255)    
) 
2. create table faculty
(
facultyid int AUTO_INCREMENT primary key,
facultyname varchar(255)    
) 
3.create table students
(
sudentid int AUTO_INCREMENT primary key,
name varchar(255),
age int, 
address text,
enrollment int,
courseid int REFERENCES course(courseid),
facultyid int REFERENCES faculty(facultyid)
) 


# Query 

 1. select coursename only bfrom table course
 2. select facultyname as staffname from table faculty
 3. select students table with coursename and facultyname 
 4. select coursename all in uppercase 

# solutions    


 ```
 select coursename from course;
 or
 select ucase(coursename) from course;
 or
 select facultyname as staffname from faculty;
 or
 select ucase(facultyname) as staffname from faculty;
 or
 select sudentid,name,age,address,coursename,facultyname from students join course on students.courseid=course.courseid join faculty on students.facultyid=faculty.facaltyid

 ```

 # user managements systems 

  1. country 
  2. state 
  3. city 
  4. users 



  # question 

  1. select only country name from country table in uppercase 
  2. select only state name from state table in uppercase 
  3. select only cityname name from city table in uppercase 
  4. select uid,uname,salary,countryname,statename,cityname from users (apply join in users table  to get all name of country , state and city)


  ## Note : create users table wth normalisation and provides cid, sid and ctid as foreign key 

# types of join

**there are 4 types of join**

1. join
2. inner join
3. outer join
    1. left join
    2. right join
    3. full join
4. cross join

#  what is join ?

1. join is used to join more than one column data with common filed if data matched one table to another tables 

**department**

|depid   | depname |
|--------|---------|
|   1    |   IT    |
|   2    |   CSE   |


**employe**

| empid  |  empname  |  age  | salary  | depid  |
|   1    |   foram   |  18   | 15000   |   1    |
|   2    |   aastha  |  19   | 16500   |   2    |
|   3    |   riya    |  19   | 20000   |   2    |
|   4    |   nirali  |  20   | 15500   |   1    |
|   5    |   piyu    |  22   | 17500   |   2    |
|   6    |   hasti   |  21   | 17000   |   1    |


# questions :  
1. write a query to create departments tables and insert 4 rows
2. write a query to fetch only depname in uppercase
3. write a query to fetch only depname in decending order
4. write a query to fetch employee details who's salary is second highest
5. write a query to fetch only details of empid 3 , 5 , 2 employee details
6. write a query to fetch only employee details who's name start with 'f' character
7. write a query to fetch depatmentname inside of employee tables with join query

# answers

1. 




# task based query 

# Part 1: The Environment Setup

# Run this script in your SQL editor to create the sandbox.
 **SQL**

CREATE TABLE Users (
user_id INT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
signup_date DATE,
country VARCHAR(50)
);
CREATE TABLE Products (
product_id INT PRIMARY KEY,
name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2),
stock_count INT
);
CREATE TABLE Orders (
order_id INT PRIMARY KEY,
user_id INT,
order_date DATE,
status VARCHAR(20),
FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE Order_Items (
item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
unit_price DECIMAL(10,2),
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
Part 2: The 100 Questions (2-Hour Timer)
The Basics (Questions 1–20)
1. Select all columns from the Users table.
2. List the names of all products in the 'Electronics' category.
3. Find all users who signed up in 2023.
4. List products with a price greater than 500.
5. Find all orders with a 'Pending' status.
6. Select the email of the user with user_id 10.
7. List all unique countries in the Users table.
8. Find products where the name starts with 'S'.
9. Get the top 5 most expensive products.
10. Find all orders placed in January 2024.
11. List users whose name contains 'John'.
12. Find products with stock_count between 10 and 50.
13. Get all orders from users in 'USA'.
14. List products sorted by price (lowest to highest).
15. Count the total number of users.
16. Find all products that are NOT in the 'Clothing' category.
17. List orders sorted by order_date descending.
18. Find users who signed up before 2022.
19. Get the names of products that cost exactly $99.99.
20. Show the first 10 rows of the Order_Items table.

# answers 

1. select * from users;

2. select name from products where category = 'Electronics';

3. select * from users where year(signup_date) = 2023;

4. select * from products where price > 500;

5. select * from orders where status = 'Pending';

6. select email from users where user_id = 10;

7. select distinct country from users;

8. select * from products where name like 'S%';

9. select * from products order by price desc limit 0,5;

10. select * from orders where month(order_date) = 1 and year(order_date) = 2024;

11. select * from users where name = 'John';

12. select * from products where stock_count between 10 and 50;

13. select * from users where country = 'USA';

14. select * from products order by price asc;

15. select count(*) from users;

16. select * from products where category != 'Clothing';

17. select * from orders order by order_date desc;

18. select * from users where signup_date < '2022-01-01';

19. select name from products where price = 99.99;

20. select * from order_items limit 0,10;