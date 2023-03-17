
## Querying the salespeople Table Using Basic Keywords in a SELECT Query

In this exercise, you will create various queries using basic keywords in a **SELECT** query. For instance, after a few days at your new job, you finally get access to the company database. Your boss has asked you to help a sales manager who does not know SQL particularly well. The sales manager
would like a couple of different lists of salespeople.


First, you need to generate a list of the first 10 salespersons hired by dealership 17, that is, the salespersons with oldest **hire_date**, ordered by hiring date, with the oldest first. 

Second, you need to get all salespeople that were hired in 2021 and 2022 but have not been terminated, that is, the **hire_date** must be later than 2021-01-01, and **terminiation_date** is **NULL**, ordered by hire date, with the latest first. 

Finally, the manager wants to find a salesperson that was hired in 2021 but
only remembers that their first name starts with "Nic." He has asked you to help find this person. You will use your SQL skill to help the manager to achieve these goals.





3. Execute the following query to get the usernames of salespeople from dealership_id 17, sorted by their hire_date values, and then set LIMIT to 10:   Usernames of 10 earliest salespeople in dealership 17 sorted by hire date
```
SELECT *
FROM salespeople
WHERE dealership_id = 17
ORDER BY hire_date
LIMIT 10;
```

### Output after running the query
![sales!](/images/sales.png)


4. Now, to find all the salespeople that were hired in 2021 and 2022 but have not been terminated, that is, the hire_date must be later than 2021-01-01, and termination_date is null, ordered by hire date, with the latest first:
```
SELECT *
FROM salespeople
WHERE hire_date >= '2021-01-01'
AND termination_date IS NULL
ORDER BY hire_date DESC;
```
54 rows are returned from this SQL. The following are the first few rows of the output:
![Active salespeople hired in 2021/2022 sorted by hire date latest first!](images/termination.png)


5. Now, find a salesperson that was hired in 2021 and whose first name starts with Nic.

```
SELECT *
FROM salespeople
WHERE first_name LIKE 'Nic%'
AND hire_date >= '2021-01-01'
AND hire_date <= '2021-12-31';
```
![Salespeople hired in 2021 and whose first name starts with Nic!](images/2021.png)


Column constraints are keywords that help you specify the properties you want to attribute to a particular column. In other words, you can ensure that all the rows in that column adhere to your   specified constraint. Some major column constraints are as follows:

- **NOT NULL**: This constraint guarantees that no value in a column can be NULL.
- **UNIQUE**: This constraint guarantees that every single row for a column has a unique value and that no value is repeated.
- **PRIMARY KEY**: This is a special constraint that is unique for each row and helps you to find a specific row more quickly. If the primary key of this table contains only one column, you can add this **PRIMARY KEY** constraint to the column definition of the primary key column. If the
primary key of this table consists of multiple columns, you need to use a table constraint to define the key in the **CREATE** statement.

## Creating a Table in SQL
In this exercise, you will create a table using the CREATE TABLE statement. The marketing team at ZoomZoom would like to create a table called countries to analyze the data of different countries. It should have four columns: an integer key column, a unique name column, a founding year column, and a capital column.

2. Execute the following query to drop the countries table since it already exists in the database:
```
DROP TABLE IF EXISTS countries;
```

3. Run the following query to create the countries table:
```
CREATE TABLE countries (
  key INT PRIMARY KEY,
	name text UNIQUE,
	founding_year INT,
	capital text
);
```

### Creating Tables with SELECT query
You already know how to create a table. However, say you wanted to create a table using data from an existing table. This can be done by using a modification of the **CREATE TABLE** statement:
```
CREATE TABLE {table_name} AS (
{select_query}
);
```
Here, **{select_query}** is any **SELECT** query that can be run in your database. For instance, say you wanted to create a table based on the **products** table that only had products from the year 2014. Suppose the title of the table is **products_2014**; you could write the following query:

```
CREATE TABLE products_2014 AS (
SELECT *
FROM products
WHERE year=2014
)
```

This can be done with any query, and the table will inherit all the properties of the output query.
PostgreSQL also provides another way to create a table from a query, which utilizes a **SELECT … INTO …**syntax. An example of this syntax is shown below:
```
SELECT *
INTO products_2014
FROM products
WHERE year=2014;
```

One issue with creating a table with a query is that the data types of the query are not explicitly specified and can be confusing. Luckily, PostgreSQL stores the table definitions in a set of system tables, and you can read the table definition from the system tables. For example, to check the column definitions of the products_2014 table, you can run the following SQL:
```
SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'products_2014';
```
From the result, you can identify all the columns and their data types in the products_2014 table:
![Query table definition from information schema!](images/product.png)


## Updating Tables
Over time, you may also need to modify a table by adding columns, adding new data, or updating existing rows. 

### Adding and Removing Columns
To add new columns to an existing table, you use the **ALTER TABLE … ADD COLUMN** statement, as shown in the following query:
```
ALTER TABLE {table_name}
ADD COLUMN {column_name} {data_type};
```

For example, if you wanted to add a new column to the **products_2014** table that you will use to store the products' weights in kilograms called **weight**, you could do this by using the following
query:
```
ALTER TABLE products_2014
ADD COLUMN weight INT;
```
This query will make a new column called **weight** in the **products_2014** table and will give it the integer data type so that only integers can be stored in it.
![ALTER statement that adds a column to a table!](images/pr.png)

If you want to remove a column from a table, you can use the **ALTER TABLE … DROP COLUMN** statement:
```
ALTER TABLE {table_name}
DROP COLUMN {column_name};
```
Here, **{table_name}** is the name of the table you want to change, and **{column_name}** is the name of the column you want to drop.

Imagine that you decide to delete the **weight** column you just
created. You could get rid of it using the following query:
```
ALTER TABLE products_2014
DROP COLUMN weight;
```
As you can see from the screenshot below, the column is dropped:
![ALTER statement that drops a column from a table!](images/weight.png)

## Adding New Data
You can add new data to a table using several methods in SQL. One of those methods is to simply insert values straight into a table using the **INSERT INTO… VALUES** statement. It has the following structure:
```
INSERT INTO {table_name} (
{column_1], {column_2}, …{column_last}
)
VALUES (
{column_value_1}, {column_value_2}, … {column_value_last}
);
```
Here, **{table_name}** is the name of the table you want to insert your data into, **{column_1}, {column_2}, … {column_last}** is a list of the columns whose values you want to insert, and **{column_value_1}, {column_value_2}, … {column_value_last}** is the list of values you want to insert into the table. If a column in the table is not put into the **INSERT** statement, the column is assumed to have a **NULL** value.

For example, say you want to insert a new entry for a scooter into the **products_2014** table. This can be done with the following query:
```
INSERT INTO products_2014 (
  product_id, model, year, product_type, base_msrp, production_start_date, production_end_date
)
VALUES (
  13, 'Nimbus 5000', 2014, 'scooter', 500.00, '2014-03-03', '2020-03-03'
);
```
This query adds a new row to the **products_2014** table accordingly. You can run a **SELECT** query to see all the rows in the table:
```
SELECT *
FROM products_2014;
```
![INSERT statement adding one row to table!](images/scooter.png)

Another way to insert data into a table is to use the **INSERT** statement with a **SELECT query** using the following syntax:
```
INSERT INTO {table_name} ({column_1], {column_2}, …{column_last})
{select_query};
```
Here, **{table_name}** is the name of the table into which you want to insert the data, **{column_1}, {column_2}, … {column_last}** is a list of the columns whose values you want to insert, and **{select query}** is a query with the same structure as the values you want to insert into the table.

Take the example of the **products_2014** table. You have created it with a **SELECT** query with one row. Earlier in this section, you have inserted one row into it. So, now it contains two rows. If you also want to insert the products from 2016, you could use the following query, which inserts one more row into the table:

```
INSERT INTO products_2014(
product_id, model, year, product_type, base_msrp,
production_start_date, production_end_date
)
SELECT*
FROM products
WHERE year=2016;
```
This query produces the following result:
![The Products_2014 table after a successful INSERT INTO query!](images/2014.png)

Now it contains three rows from three different ways of inserting data: one row from **CREATE** as the result of a **SELECT** query, one row from an **INSERT** with data, and one row from **INSERT** using the result of a **SELECT** query.

## Updating existing rows
Sometimes, you may need to update the values of the data present in a table. To do this, you can use the **UPDATE** statement:
```
UPDATE {table_name} SET
{column_1} = {column_value_1},
{column_2} = {column_value_2},
…
{column_last} = {column_value_last}
WHERE {conditional};
```
Here, **{table_name}** is the name of the table with data that will be changed, **{column_1}, {column_2},… {column_last}** is the list of columns whose values you want to change, **{column_value_1}, {column_value_2}, … {column_value_last}** is the list of new values you want to update into those columns, and **{WHERE}** is a conditional statement like the one you would find in a **SELECT** query.

To illustrate its use of the **UPDATE** statement, imagine that, for the rest of the year, the company has decided to sell all scooter models before 2018 for $299.99. You could change the data in the **products_2014** table using the following query:
```
UPDATE Products_2014 SET
base_msrp = 299.99
WHERE product_type = 'scooter'
AND year<2018;
```
This query produces the following output. You can see that the **base_msrp** column of all three records has been updated to **299.99** because they are all scooters manufactured before 2018.
![Successful update of the products_2014 table!](images/299.png)

## Updating the Table to Increase the Price of a Vehicle
You will update the data in a table using the **UPDATE** statement. Due to an increase in the cost of the rare metals needed to manufacture an electric vehicle, the 2022 Model Chi will need to undergo a price hike of 10%. The current price is $95,000.

In a real-world scenario, you will update the **products** table to increase the price of this product. However, because you will use the same **sqlda** database throughout, it would be better to keep the values in the original tables unchanged so that your SQL results remain consistent. For this reason, you will create new tables for all the **INSERT, ALTER, UPDATE, DELETE,** and **DROP** statement examples.

Perform the following steps to complete the exercise:
1. Open **pgAdmin**, connect to the **sqlda** database, and open SQL query editor.
2. Run the following query to create a **product_2022** table from the **products** table:
```
CREATE TABLE products_2022 AS (
  SELECT *
	FROM products
	WHERE year=2022
);
```
3. Run the following query to update the price of Model Chi by 10% in the **products_2022** table:
```
UPDATE products_2022 SET
  base_msrp = base_msrp*1.10
  WHERE model='Model Chi'
  AND year=2022;
```
 4. Write the **SELECT** query to check whether the price of Model Chi in 2022 has been updated: 
```
SELECT *
FROM products_2022
WHERE model='Model Chi'
AND year=2022;
```
The following is the output of the preceding code:
![The updated price of Model Chi in 2022!](images/model.png)

As you see from the output, the price of Model Chi is now $104,500; it was previously $95,000.

## Deleting Data and Tables
You often discover that data in a table is out of date and, therefore, can no longer be used. At such times, you might need to delete data from a table.
### Deleting Values from a Row
Often, you might be interested in deleting a value from a row. The easiest way to accomplish this is to use the **UPDATE** structure that has already been discussed, and by setting the column value to **NULL**:
```
UPDATE {table_name} SET{column_1} = NULL,
{column_2} = NULL,
…
{column_last} = NULL
WHERE {conditional};
```
Here, **{table_name}** is the name of the table with the data that needs to be changed, **{column_1}, {column_2},… {column_last}** is the list of columns whose values you want to delete, and **{WHERE}** is a conditional statement like the one you would find in a **SELECT** query.

For instance, you have the wrong email address on file for the customer with the **customer ID** equal to **3**. To fix that, you can use the following query:
```
UPDATE customers SET
email = NULL
WHERE customer_id=3;
```
However, there might be cases where you might need to delete rows from a table. For example, in the database, you have a row labeled **test customer**, which is no longer needed and needs to be deleted. 

### Deleting Rows from a Table
Deleting a row from a table can be done using the **DELETE** statement, which looks like this:
```
DELETE FROM {table_name}
WHERE {condition};
```
For instance, you must delete the products whose **product_type** is **scooter** from the **products_2014** table. To do that, you can use the following query:
```
DELETE FROM products_2014
WHERE product_type='scooter';
```
You have inserted three products into this table, all scooters. After running the **DELETE** statement, PostgreSQL shows that there was no product in this table anymore as all records are deleted.
![DELETE statement example!](images/scooter.png)

If you want to delete all the data in the **products_2014** table without deleting the table, you could write the following query, which is **DELETE** without any conditions:
```
DELETE FROM products_2014;
```
Alternatively, if you want to delete all the data in a query without deleting the table, you could use the **TRUNCATE** keyword like so:
```
TRUNCATE TABLE products_2014;
```

### Deleting Tables
To delete all the data in a table and the table itself, you can just use the **DROP TABLE** statement with the following syntax:
```
DROP TABLE {table_name};
```
Here, **{table_name}** is the name of the table you want to delete. If you wanted to delete all the data in the **products_2014** table along with the table itself, you would write the following:
```
DROP TABLE products_2014;
```
If you want to read from this table, you will receive an error message from PostgreSQL telling you that the table does not exist:
```
DROP TABLE products_2014;

SELECT * FROM products_2014;
```
![DROP statement example!](images/drop.png)

Once the table is dropped, all aspects of this table are gone, and you cannot perform any operations on it. For example, if you try to run the **DROP TABLE products_2014** statement again, you will run into an error. A PostgreSQL enhancement of the **DROP** statement is **DROP TABLE IF EXISTS**. This statement will check the existence of the table. If the table is not in the database, PostgreSQL will skip this statement with a notification, but without reporting an error, as shown below:
```
DROP TABLE IF EXISTS products_2014;
```
![DROP TABLE IF EXISTS statement example!](images/drop1.png)
**DROP TABLE IF EXISTS** is helpful if you want to automate SQL script execution. One common usage scenario is to use it before the **CREATE TABLE** statement. If the table already exists, your **CREATE TABLE** statement will fail and raise an error. But if your **DROP TABLE IF EXISTS**
statement is before your **CREATE TABLE** statement, pre-existing tables would have been dropped before you tried to recreate them. This is useful in automated computing operations where you constantly create temporary tables that you do not need after the current computing job is completed.

The catch is that you must make sure that the table is truly temporary and is not used by anyone else. Otherwise, you may accidentally drop tables that are used by some other users without knowing. For this reason, the **DROP TABLE IF EXISTS** statement is usually only used in environments
designated for automated data processing.

### Deleting an Unnecessary Reference Table
you will learn how to delete a table using SQL. For instance, the marketing team has finished analyzing the potential number of customers they have in every state, and they no longer need the **state_populations** table. To save space in the database, delete the table. If you have not
created this table, please go back to the Simple CREATE Statement and create it now.
1. Open pgAdmin, connect to the **sqlda database**, and open **SQL query editor**.
2. Run the following query to drop the **state_populations** table:
```
DROP TABLE state_populations;
```
3. Check that the **state_populations** table has been deleted from the database.
4. Since the table has just been dropped, a **SELECT** query on this table throws an error, as expected:
```
SELECT * FROM state_populations;
```
You will find the error in the following figure: 
![Error shown as the state_populations table was dropped!](images/state.png)

5. Also, drop the **products_2022** table that was created above to keep the database clean:
```
DROP TABLE products_2022;
```

### Creating and Modifying Tables for Marketing Operations
You did a great job of pulling data for the marketing team. However, the marketing manager, who you helped, realized that they had made a mistake. It turns out that instead of just the query, the manager needs to create a new table in the company's analytics database. Furthermore, they need to make some changes to the data that is present in the **customers table**. It is your job to help the marketing manager with the table:

1. Open pgAdmin, connect to the **sqlda** database and open SQL query editor. Create a new table called **customers_nyc** that pulls all the rows from the **customers** table where the customer lives in New York City in the state of New York.

```
CREATE TABLE customers_nyc AS (
SELECT *
FROM customers
WHERE city='New York City'
AND state='NY'
);
```
Run the following code to see the output:
```
SELECT * FROM customers_nyc;
```
This is the output of the code:
![Table showing customers from New York City!](images/nyc.png)

2. Delete all customers in postal code 10014 from the new table. Due to local laws, they will not be eligible for marketing.
Run the following query statement to delete users with the postal code 10014:
```
DELETE FROM customers_nyc
WHERE postal_code='10014';
```

3. Add a new text column called **event**.
Execute the following query to add the new **event** column:
```
ALTER TABLE customers_nyc
ADD COLUMN event text;
```

4. Set the value of the event column to **thank-you party**.
Update the **customers_nyc** table and set the **event** column to **thank-you party** using the following query:
```
UPDATE customers_nyc SET
event = 'thank-you party';
```
Run the following code to see the output:
```
SELECT *
FROM customers_nyc;
```
The following is the output of the code:
![The customers_nyc table with event set to thank-you party!](images/event.png)

You tell the manager that you have completed these steps. He tells the marketing operations team, who then uses the data to launch a marketing campaign. The marketing manager then asks you to delete the **customers_nyc** table.

Delete the **customers_nyc** table as asked by the manager using **DROP TABLE**:
```
DROP TABLE customers_nyc;
```


# SQL for Data Preparation
In the real world, as a data analyst, you usually do not handle the entire CRUD flow. To be more specific, you usually do not create datasets from scratch. You will receive data from outside sources. This data is usually in a form that would not fit your needs perfectly and you would need to perform some transform operations to make the data usable. One such operation is the creation of clean datasets from existing raw datasets. The raw data may be missing some information, contain information that is not in the format that fits your needs, or contains information that may not be accurate.

According to Forbes, it is estimated that almost 80% of the time spent by analytics professionals involves preparing data. Building models with unclean data harms analysis by leading to poor conclusions. SQL can help in this tedious but important task by providing efficient ways to build clean datasets.

## Assembling Data
### Connecting Tables using JSON
Most of the time, the data you are interested in is spread across multiple tables. A simple **SELECT** statement over one table will not be enough to get you what you need. Fortunately, SQL has methods for bringing related tables together using the **JOIN** keyword.

To illustrate, look at two tables in the **ZoomZoom** database—**dealerships** and **salespeople**.
![Structure of dealerships table!](images/DEALERSHIP.png)

And the **salespeople** table looks like this:
![Structure of salespeople table!](images/salespeople.png)

In the **salespeople** table, you can observe that there is a column called **dealership_id**. This **dealership_id** column is a direct reference to the **dealership_id** column in the **dealerships** table.

When table A has a column that references the primary key of table B, the column is said to be a foreign key to table A. In this case, the **dealership_id** column in salespeople is a foreign key to the dealerships table.

**Note**
*Foreign keys can also be added as a column constraint to a table to improve the integrity of the data by making sure that the foreign key never contains a value that cannot be found in the referenced table. This data property is known as **referential integrity**. The method of adding foreign key constraints can also help to improve performance in some databases. Foreign key constraints are not used in most analytical databases and are beyond the scope of this text. You can learn more about
foreign key constraints in the official PostgreSQL documentation.*

As these two tables are related, you can perform some interesting analyses with them. 

For instance, you may be interested in determining which salespeople work at a dealership in California. One way of retrieving this information is to first query which dealerships are in California. You can do this using the following query:
```
SELECT *
FROM dealerships
WHERE state='CA';
```
This query should give you the following results:
![Dealerships in California!](images/ca.png)

Now that you know that the only two dealerships in California have the IDs of **2** and **5**, respectively, you can then query the **salespeople** table, as follows:
```
SELECT *
FROM salespeople
WHERE dealership_id in (2, 5)
ORDER BY 1;
```
The following are the first rows of the output of the code:
![Salespeople in California!](images/sa.png)

While this method gives you the results you want, it is tedious to perform two queries to get these results. What would make this process easier would be to somehow add the information from the **dealerships** table to the **salespeople** table and then filter for users in California. SQL provides such a tool with the **JOIN** clause. The **JOIN** clause is a SQL clause that allows a user to join one or more tables together based on distinct conditions.

### Types of Joins
![Major types of joins!](images/joins.png)

## Inner Joins
An inner join connects rows in different tables, based on a condition known as the **join predicate**. In many cases, the join predicate is a logical condition of equality. Each row in the first table is compared
against every other row in the second table. For row combinations that meet the inner join predicate, that row is returned in the query. Otherwise, the row combination is discarded.

Inner joins are usually wriiten in the following form:
```
SELECT {columns}
FROM {table1}
INNER JOIN {table2}
  ON {table1}.{common_key_1}={table2}.{common_key_2};
```
Here, **{columns}** is the columns you want to get from the joined table, **{table1}** is the first table, **{table2}** is the second table, **{common_key_1}** is the column in **{table1}** you want to join on, and **{common_key_2}** is the column in **{table2}** to join on.

Now, go back to the two tables discussed previously—**dealerships** and **salespeople**. As mentioned earlier, it would be good if you could append the information from the **dealerships** table to the **salespeople** table knowing which state each dealership is in. For the time being, assume that all the salespeople IDs have a valid **dealership_id** value.

You can join the two tables using an equal to condition in the join predicate, as follows:
```
SELECT *
FROM salespeople
INNER JOIN dealerships
ON salespeople.dealership_id = dealerships.dealership_id
ORDER BY 1;
```

The following figure shows the first few rows of the output:
![The salespeople table joined to the dealerships table!](images/id.png)

As you can see in the preceding output, the table is the result of joining the **salespeople** table to the **dealerships** table. Note that the first table listed in the query, **salespeople**, is on the left-
hand side of the result, while the **dealerships** table is on the right-hand side. 

This left-right order will become very important when you learn about outer joins between tables. During an outer join, whether a table is on the left or right side can impact the output of the query. For an inner join, however, the order of tables is not important for join predicates that use an equal operation.

Now, look at the columns involved; **dealership_id** in the **salespeople** table matches **dealership_id** in the **dealerships** table. This shows how the join predicate is met. By
running this **join** query, you have effectively created a new "super dataset" consisting of the two tables merged where the two **dealership_id** columns are equal.

You can now run a **SELECT** query over this "super dataset" in the same way as one large table using the clauses and keywords from before.

For example, going back to the multi-query issue to determine which sales query works in California, you can now address it with one easy query:
```
SELECT *
FROM salespeople
INNER JOIN dealerships
ON salespeople.dealership_id = dealerships.dealership_idWHERE dealerships.state = 'CA'
ORDER BY 1;
```
This gives you the following output, which displays the first few rows of the entire result set:
![Salespeople in California with one query!](images/ca%20rep.png)

If you want to retrieve only the **salespeople** table portion of this, you can select the **salespeople** columns using the following star syntax
```
SELECT salespeople.*
FROM salespeople
INNER JOIN dealerships
  ON dealerships.dealership_id = salespeople.dealership_id
WHERE dealerships.state = 'CA'
ORDER BY 1;
```
Here are the first few rows returned by this query:
![Salespeople in California with SELECT table alias!](images/sel.png)

There is another shortcut that can help while writing statements with several **JOIN** clauses. You can alias table names to avoid typing the entire name of the table every time. Simply write the name of the alias after the first mention of the table after the **JOIN** clause, and you can save a decent amount of typing. 

For instance, for the preceding query, if you wanted to alias salespeople with s and dealerships with d, you could write the following statement:
```
SELECT s.*
FROM salespeople s
INNER JOIN dealerships d
  ON d.dealership_id = s.dealership_id
WHERE d.state = 'CA'
ORDER BY 1;
```
Alternatively, you could also put the **AS** keyword between the table name and alias to make the alias more explicit:
```
SELECT s.*
FROM salespeople AS s
INNER JOIN dealerships AS d
ON d.dealership_id = s.dealership_id
WHERE d.state = 'CA'
ORDER BY 1;
```


## Outer Joins
Inner joins will only return rows from the two tables when the join predicate is met for both tables, that is, when both tables have rows that can satisfy the join predicate. Otherwise, no rows from either table are returned. 

It can happen that sometimes you want to return all rows from one of the tables, even if the other table does not have any row meeting the join predicate. In this case, since there is no row meeting the join predicate, the second table will return nothing but **NULL**. Outer join is a join type in which all rows from at least one table, if meeting the query **WHERE** condition, will be presented after the **JOIN** operation.

Outer joins can be classified into three categories: left outer joins, right outer joins, and full outer joins:

- Left outer join: **Left outer joins** are where the left table (that is, the table mentioned first in a join clause) will have every row returned. If a row from the other table (the right table) is not
found, a row of **NULL** is returned from the right table. Left outer joins are performed by using the **LEFT OUTER JOIN** keywords, followed by a join predicate. This can also be written in short as **LEFT JOIN**.


To show how left outer joins work, examine two tables: the **customers** table and the **emails table**. For the time being, assume that not every customer has been sent an email, and you want to mail all customers who have not received an email. You can use a left outer join to make that happen since the left side of the join is the **customers** table. To help manage the output, you will limit it to the first 1,000 rows. The following code snippet is utilized:
```
SELECT
 *
FROM
  customers c
LEFT OUTER JOIN
  emails e ON e.customer_id=c.customer_id
ORDER BY
  c.customer_id
LIMIT 1000;
```
The following is the output of the preceding code:
![Customers left-joined to emails!](images/leftjoin.png)

When you look at the output of the query, you should see that entries from the **customers** table are present. However, for some of the rows, such as for **customer_id 27**, which can be seen above, the columns belonging to the **emails** table are completely full of **NULL** values. This arrangement explains how the outer join is different from the inner join. 

If the inner join was used, the **customer_id 27** row would not show because there is no matching record in the emails table.

This query, however, is still useful because you can now use it to find people who have never received an email. Because those customers who were never sent an email have a null **customer_id** column in the values returned from **emails** table, you can find all these customers by checking the **customer_id** column in the **emails** table, as follows:
```
SELECT
   c.customer_id,
   c.title,
   c.first_name,
   c.last_name,
   c.suffix,
   c.email,e.email_id,
   e.email_subject,
   e.opened,
   e.clicked,
   e.bounced,
   e.sent_date,
   e.opened_date,
   e.clicked_date
FROM
  customers c
LEFT OUTER JOIN
  emails e ON c.customer_id = e.customer_id
WHERE
  e.customer_id IS NULL
ORDER BY
  c.customer_id
LIMIT
  1000;
```
The following is the output of the query:
![Customers with no emails sent!](images/mail.png)

As you can see, all entries are blank in the **email_id** column of the **emails** table, indicating that the customer of that row has not received any emails. You could simply grab the emails from this join to get all the customers who have not received an email.

- Right outer join: A **right outer join** is very similar to a left join, except the table on the "right" (the second listed table) will now have every row show up, and the "left" table will have **NULL** values if the **JOIN** condition is not met. To illustrate, let's "flip" the last query by right-joining the **emails** table to the **customers** table with the following query:
```
SELECT
  e.email_id,
  e.email_subject,
  e.opened,
  e.clicked,
  e.bounced,
  e.sent_date,
  e.opened_date,
  e.clicked_date,
  c.customer_id,c.title,
  c.first_name,
  c.last_name,
  c.suffix,
  c.email
FROM emails e
RIGHT OUTER JOIN customers c
  ON e.customer_id=c.customer_id
ORDER BY
  c.customer_id
LIMIT
  1000;
```
When you run this query, you will get something similar to the following result:
![Emails right-joined to the customers table!](images/rightjoin.png)

Notice that this output is similar to what was produced above, except that the data from the **emails** table is now on the left-hand side, and the data from the **customers** table is on the right-hand side. Once again, **customer_id 27** has **NULL** for the email. This shows the symmetry between a right join and a left join.

- Full outer join: Finally, there is the ***full outer join**. The full outer join will return all rows from the left and right tables, regardless of whether the join predicate is matched. For rows where the
join predicate is met, the two rows are combined just like in an inner join. For rows where it is not met, each row from both tables will be selected as an individual row, with **NULL** filled in for the columns from the other table. The full outer join is invoked by using the **FULL OUTER JOIN** clause, followed by a join predicate. Here is the syntax of this join:
```
SELECT
*
FROM
  emails e
FULL OUTER JOIN
  customers c
  ON e.customer_id=c.customer_id;
```
The following is the output of the code:
![Emails are full outer joined to the customers table!](images/fulloutrt.png)

## Cross Joins












