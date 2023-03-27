
## Querying the salespeople Table Using Basic Keywords in a SELECT Query

You will create various queries using basic keywords in a **SELECT** query. For instance, after a few days at your new job, you finally get access to the company database. Your boss has asked you to help a sales manager who does not know SQL particularly well. The sales manager
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
Cross join is a join type that has no join predicate. That means every row from the "left" table will be matched to all the rows in the "right" table, regardless of whether they are related or not. It is also
referred to as the Cartesian product. It is named "Cartesian" after the French mathematician René Descartes, who raised the idea of this type of operation. It can be invoked using a **CROSS JOIN** clause, followed by the name of the other table. To better understand this, take the example of the **products** table.

A common analysis is called market basket analysis, which studies the selling patterns between multiple products. For example, diapers are usually sold together with baby wipes. So, if you are running a two-month giveaway for diapers for marketing purposes and expect more customers to
come to the diaper aisle or web page, you may want to place baby wipes there too. To perform market basket analysis, you want to know every possible combination of two products that you could create from a given set of products (such as the ones found in the products table) to create a two-month giveaway for marketing purposes. You can use a cross join to get the answer to the question using the following query:
```
SELECT
  P1.product_id, p1.model,
  P2.product_id, p2.model
FROM
  products p1
CROSS JOIN
  products p2;
```
The output of this query is as follows:
![The cross join of a product to itself!](images/CR.png)

In this case, you have joined every value of every field in one table to the same in another table. The result of the query has 144 rows, which is the equivalent of multiplying the 12 products by the same 12 products (12 * 12). You can also see that cross join does not require a join predicate. In other words, a cross join can simply be thought of as just an outer join with no conditions for joining.

In general, cross joins are not used much in practice as they can hamper the process if you are not careful. Cross joining two large tables can lead to the origination of hundreds of billions of rows, which can stall and crash a database. So, if you decide to use a cross join, ensure you take utmost care when using it.


## Using Joins to Analyze Sales Dealership
You will use joins to bring related tables together. For instance, the head of sales at your company would like a list of all customers who bought a car. To do the task, you need to create a query that will return all customer IDs, first names, last names, and valid phone numbers of customers who purchased a car.


1. Open **pgAdmin**, connect to the **sqlda** database, and open SQL query editor.
2. Use an inner join to bring the **sales**, **customers**, and **products** tables together, which returns data for customer IDs, first names, last names, and valid phone numbers:
```
SELECT
  c.customer_id, c.first_name,
  c.last_name, c.phone
FROM
  sales s
INNER JOIN
  customers c ON c.customer_id=s.customer_id
INNER JOIN
  products p ON p.product_id=s.product_id
WHERE
  p.product_type='automobile'
  AND c.phone IS NOT NULL;
```
You should get an output similar to the following:
![Customers who bought a car!](images/CAR.png)

You can see that running the query helped you to join the data from the **sales**, **customers**, and **products** tables and obtain a list of customers who bought a car and have a phone number.

You were able to bring together related tables easily and efficiently.
Several times, you will also want to combine the result of your queries to form new queries so that you can build data analysis on top of existing analysis.

## Subqueries
So far, you have been pulling data from tables. You may have observed that the results of all **SELECT** queries are two-dimensional relations that look like the tables in a relational database. Knowing this,
you may wonder whether there is some way to use the relations produced by the **SELECT** queries instead of referencing an existing table in your database. The answer is "yes." You can simply take a query, insert it between a pair of parentheses, and give it an alias. This will help you to build an analysis on top of existing analysis, thus reducing errors and improving efficiency.

For example, if you wanted to find all the salespeople working in California and get the results the same as ![above!](https://github.com/Esther-Wavinya/Python-Crash-Course-Assignment/blob/main/sql/images/ca%20rep.png), you could write the query using the following alternative:
```
SELECT
  *
FROM
  salespeople
INNER JOIN (
  SELECT
   *
FROM
    dealerships
WHERE
    dealerships.state = 'CA'
) d
ON d.dealership_id = salespeople.dealership_id
ORDER BY
  1;
```

Here, instead of joining the two tables and filtering for rows with the state equal to **'CA'**, you first find the dealerships where the state equals **'CA'**, and then inner join the rows in that query to
**salespeople**.

If a query only has one column, you can use a subquery with the **IN** keyword in a **WHERE** clause. For example, another way to extract the details from the **salespeople** table using the dealership ID for
the state of California would be as follows:
```
SELECT
  *
FROM
  salespeople
WHERE dealership_id IN (
  SELECT dealership_id FROM dealerships
  WHERE dealerships.state = 'CA'
)
ORDER BY
  1;
```
As illustrated in all of these examples, it is quite easy to write the same query using multiple techniques.


# Unions
You have learned how to join data horizontally. You can use joins to add
new columns horizontally. However, you may be interested in putting multiple queries together vertically, that is, by keeping the same number of columns but adding multiple rows. Please see this example for more clarity on this.

Suppose you wanted to visualize the addresses of dealerships and customers using Google Maps. To do this, you would need the addresses of both customers and dealerships. You could build a query with all customer addresses as follows:
```
SELECT
  street_address, city, state, postal_code
FROM
  customers
WHERE
  street_address IS NOT NULL;
```

You could also retrieve dealership addresses with the following query:
```
SELECT
  street_address, city, state, postal_code
FROM
  dealerships
WHERE
  street_address IS NOT NULL;
```

To reduce complexity, it would be nice if there were a way to assemble the two queries into one list with a single query. This is where the **UNION** keyword comes into play. You can use the two previous
queries and create the following query:
```
(
SELECT
  street_address, city, state, postal_code
FROM
  customers
WHERE
  street_address IS NOT NULL
)
UNION
(
SELECT
  street_address, city, state, postal_code
FROM
  dealerships
WHERE
  street_address IS NOT NULL
)
ORDER BY
  1;
```  

This produces the following output:
![Union of addresses!](images/un.png)

Please note that there are certain conditions that need to be kept in mind when using **UNION**. 

Firstly, **UNION** requires the subqueries to have the same number of columns and the same data types for the columns. If they do not, the query will fail to run. 

Secondly, **UNION** technically may not return all the rows from its subqueries. 

**UNION**, by default, removes all duplicate rows in the output. If you want to retain the duplicate rows, it is preferable to use the **UNION ALL** keyword.

For example, if both of the previous queries return a row with address values such as '123 Main St', 'Madison', 'WI', '53710', the result of the **UNION** statement will only contain one record for this value set, but the result of the **UNION ALL** statement will include two records of the same value, one from each query.

### Generating an Elite Customer Party Guest List Using UNION
You will assemble two queries using **UNION**. 

To help build marketing awareness for the new **Model Chi**, the marketing team would like to throw a party for some of ZoomZoom's 
wealthiest customers in Los Angeles, CA. To help facilitate the party, they would like you to make a guest list with ZoomZoom customers who live in Los Angeles, CA, as well as salespeople who work at the ZoomZoom dealership in Los Angeles, CA. The guest list should include details such as the first and last names and whether the guest is a customer or an employee.

1. Open **pgAdmin**, connect to the **sqlda** database, and open the SQL query editor.

Write a query that will make a list of ZoomZoom customers and company employees who live in Los Angeles, CA. The guest list should contain first and last names and whether the guest is a customer or an employee:
```
(
SELECT
  first_name, last_name, 'Customer' as guest_type
FROM
  customers
WHERE
  city='Los Angeles'
  AND state='CA'
)
UNION
(
SELECT
  first_name, last_name,
  'Employee' as guest_type
FROM
  salespeople s
INNER JOIN
  dealerships d ON d.dealership_id=s.dealership_id
WHERE
  d.city='Los Angeles'
  AND d.state='CA'
);
```
You should get the following output:
![Customer and employee guest list in Los Angeles, CA!](images/li.png)

You can see the guest list of customers and employees from Los Angeles, CA, after running the **UNION** query.

2. To demonstrate the usage of **UNION ALL**, first run a simple query that combines the **products** table with all the rows:
```
SELECT * FROM products
UNION
SELECT * FROM products
ORDER BY 1;
```
![the query returns 12 rows and there are no duplicated rows!](images/rows.jpg)

You can see that the query returns 12 rows and there are no duplicated rows, just the same as the original **products** table. However, say you run the following query:
```
SELECT * FROM products
UNION ALL
SELECT * FROM products
ORDER BY 1;
```
![24 rows!](images/24.jpg)

You will see that the query returns 24 rows, in which each row is repeated twice. This is because the **UNION ALL** statement keeps the duplicated rows from both **products** tables.


# Common Table Expressions
CTEs are simply a different version of subqueries. CTEs establish temporary tables by using the **WITH** clause. To understand this clause better, look at the following query, which you used before to find
California-based salespeople:
```
SELECT
  *
FROM
  salespeople
INNER JOIN (
  SELECT
    *
FROM
   dealerships
WHERE
   dealerships.state = 'CA'
) d
ON d.dealership_id = salespeople.dealership_id
ORDER BY
   1;
```
This could be written using CTEs, as follows:
```
WITH d as (
  SELECT
    *
  FROM
    dealerships
  WHERE
    dealerships.state = 'CA'
)
SELECT
  *
FROM
  salespeople
INNER JOIN
  d ON d.dealership_id = salespeople.dealership_id
ORDER BY
  1;
```   

The one advantage of CTEs is that they can be designed to be recursive. **Recursive CTEs** can reference themselves. Because of this feature, you can use them to solve problems that other queries cannot. However, recursive CTEs are beyond the scope of this text.


Now that you know several ways to join data across a database, look at how to transform the data from these outputs.


# Cleaning Data
Often, the raw data presented in a query output may not be in the desired form. You may want to remove values, substitute values, or map values to other values. To accomplish these tasks, SQL provides a wide variety of statements and functions. 

**Functions** are keywords that take in inputs (such as a column or a scalar value) and process those inputs into some sort of output. You will learn about some useful functions for data transformation and cleaning in the following text.

## The CASE WHEN Function
**CASE WHEN** is a function that allows a query to map various values in a column to other values. The general format of a **CASE WHEN** statement is as follows:
```
CASE
   WHEN condition1 THEN value1
   WHEN condition2 THEN value2
   …
   WHEN conditionX THEN valueX
   ELSE else_value
END;
```
Here, **condition1** and **condition2**, through **conditionX**, are **Boolean** conditions; **value1** and **value2**, through **valueX**, are values to map to the Boolean conditions; and **else_value** is the value that is mapped if none of the Boolean conditions is met. 

For each row, the program starts at the top of the **CASE WHEN** statement and evaluates the first Boolean condition. The program then
runs through each Boolean condition from the first one. For the first condition from the start of the statement that evaluates as **True**, the statement will return the value associated with that condition. If
none of the statements evaluates as **True**, then the value associated with the **ELSE** statement will be returned.

For example, you want to return all rows for **customers** from the **customers** table. Additionally, you would like to add a column that labels a user as being an **Elite Customer** type if they live in
postal code **33111**, or as a **Premium Customer** type if they live in postal code **33124**. Otherwise, it will mark the customer as a **Standard Customer** type. This column will be called
**customer_type**. You can create this table by using a **CASE WHEN** statement, as follows:
```
SELECT
 CASE
   WHEN postal_code='33111' THEN 'Elite Customer'
   WHEN postal_code='33124' THEN 'Premium Customer'
   ELSE 'Standard Customer'
 END AS customer_type,
 *
FROM customers;
```
This query should give the following output:
![The customer_type query!](images/query.png)

As you can see in the preceding table, there is a column called **customer_type** indicating the type of customer a user is. The **CASE WHEN** statement effectively mapped a postal code to a string
describing the customer type. Using a **CASE WHEN** statement, you can map values in any way you please.

## Using the CASE WHEN Function to Get Regional Lists
The aim of this exercise is to create a query that will map various values in a column to other values. 

For instance, the head of sales has an idea to try and create specialized regional sales teams that will be able to sell scooters to customers in specific regions, as opposed to generic sales teams. To make their idea a reality, the head of sales would like a list of all customers mapped to regions. For customers from the states of MA, NH, VT, ME, CT, or RI, they would like them labeled as New England. Customers from the states of GA, FL, MS, AL, LA, KY, VA, NC, SC, TN, VI, WV, or AR,they would like the customers labeled as Southeast. Customers from any other state should be
labeled as Other.

1. Open **pgAdmin**, connect to the **sqlda** database, and open the SQL query editor.
2. Create a query that will produce a **customer_id** column and a column called **region**, with the states categorized as in the following scenario:
```
SELECT
  c.customer_id,
  CASE
    WHEN c.state in (
'MA', 'NH', 'VT', 'ME', 'CT', 'RI') THEN 'New England'
    WHEN c.state in (
'GA', 'FL', 'MS', 'AL', 'LA', 'KY', 'VA', 'NC', 'SC', 'TN', 'VI',
'WV', 'AR') THEN 'Southeast'
ELSE 'Other'
   END as region
FROM
   customers c
ORDER BY
   1;
```
This query will map a state to one of the regions based on whether the state is in the **CASE WHEN** condition listed for that line. You should get the following output:
![The regional query output!](images/REGIONAL.png)
In the preceding output, in the case of each customer, a region has been mapped based on the state where the customer resides.

In this exercise, you learned how to map various values in a column to other values using the **CASE WHEN** function. In the next section, you will learn about a useful function, **COALESCE**, which will
help to replace the **NULL** values.

## The COALESCE Function
Another common requirement is to replace the **NULL** values with a standard value. This can be accomplished easily by means of the **COALESCE** function. 

**COALESCE** allows you to list any number of columns and scalar values, and, if the first value in the list is **NULL**, it will try to fill it in with the second value. The **COALESCE** function will keep continuing down the list of values until it hits a non-**NULL** value. If all values in the **COALESCE** function are **NULL**, then the function returns **NULL**.

To illustrate a simple usage of the **COALESCE** function, study the **customers** table. Some of the records do not have the value of the **phone** field populated:
```
SELECT *
FROM customers;
```
![The COALESCE query!](images/phone.png)

For instance, the marketing team would like a list of the first names, last names, and phone numbers of all customers for a survey. However, for customers with no phone number, they would like the table to
instead write the value **NO PHONE**. You can accomplish this request with **COALESCE**:
```
SELECT
   first_name, last_name,
   COALESCE(phone, 'NO PHONE') as phone
FROM
   customers
ORDER BY 1;
```
This query produces the following results:
![The COALESCE query!](images/coalesce.png)

When dealing with creating default values and avoiding **NULL**, **COALESCE** will always be helpful.

## The NULLIF Function
**NULLIF** is used as the opposite of **COALESCE**. While **COALESCE** is used to convert **NULL** into a standard value, **NULLIF** is a two-value function and will return **NULL** if the first value equals the
second value.

For example, the marketing department has created a new direct mail piece to send to the customer. One of the quirks of this new piece of advertising is that it cannot accept people who have titles (Mr,
Dr, Mrs, and so on) longer than three letters. However, some records may have a title that is longer than three letters. If the system cannot accept them, they should be removed during the retrieval of results.

In the sample database, the only known title longer than three characters is **Honorable**. Therefore, they would like you to create a mailing list that is just all the rows with valid street addresses and to
block out all titles with **NULL** that are spelled as **Honorable**. This could be done with the following query:
```
SELECT customer_id,
     NULLIF(title, 'Honorable') as title,
     first_name,
     last_name,
     suffix,email,
     gender,
     ip_address,
     phone,
     street_address,
     city,
     state,
     postal_code,
     latitude,
     longitude,
     date_added
FROM
     customers c
ORDER BY 1;
```

This will remove all mentions of **Honorable** from the **title** column.
![The NULLIF query!](images/nullify.png)

## The LEAST/GREATEST Functions
Two functions that come in handy for data preparation are the **LEAST** and **GREATEST** functions. Each function takes any number of values and returns the least or the greatest of the values, respectively. 

For example, if you use the **LEAST** function with two parameters, such as 600 and 900, 600 will be returned as the value. It is the opposite of what the GREATEST function will return. The parameters can either be literal values or the values stored inside numeric fields.

The simple use of this variable would be to replace the value if it is too high or low. You can study an example closely to understand it better. For instance, the sales team may want to create a sales list
where every scooter is $600 or less. You can create this using the following query:
```
SELECT
    product_id, model,
    year, product_type,
    LEAST(600.00, base_msrp) as base_msrp,
    production_start_date,
    production_end_date
FROM
    products
WHERE
    product_type='scooter'
ORDER BY 1;
```
This query should give the following output:
![Cheaper scooters!](images/sco.png)

From the output, you can see that if **base_msrp** was lower than **600**, the SQL query will return the original **base_msrp**. But if **base_msrp** is higher than **600**, you will get **600** back. It is the lower value of **base_msrp** and **600** that the query returns, which is what the **LEAST()** function is supposed to do.



## The Casting Function
Another useful data transformation is to change the data type of a column within a query. This is usually done to use a function only available to one data type, such as text, while working with a
column that is in a different data type, such as numeric. To change the data type of a column, you simply need to use the **column::datatype** format, where column is the **column** name and **datatype** is the **datatype** you want to change the column to.

For example, to change the year in the **products** table to a text column in a query, use the following query:
```
SELECT
   product_id,
   model,
   year::TEXT,
   product_type,
   base_msrp,
   production_start_date,
   production_end_date
FROM
   products;
```
This query produces the following output:
![The year column as text!](images/year.png)

This will convert the **year** column to text. You can now apply text functions to this transformed column. Please note that not every data type can be cast to a specific data type. For instance,**datetime** cannot be cast to float types. Your SQL client will throw an error if you ever make an unexpected conversion.


# Transforming Data
Each dataset is unique along with each of the business use cases for the datasets. That means the processing and transforming of datasets are unique in their own way. However, there are some processing logics that you will frequently run into in the real world. 

## The DISTINCT AND DISTINCT ON Functions
When looking through a dataset, you may be interested in determining the unique values in a column or group of columns. This is the primary use case of the **DISTINCT** keyword.

For example, if you wanted to know all the unique model years in the **products** table, you could use the following query:
```
SELECT DISTINCT year
FROM products
ORDER BY 1;
```
This should give the following result:
![Distinct model years!](images/distinct.png)

You can also use it with multiple columns to get all the distinct column combinations present. For example, to find all distinct years and what product types were released for those model years, you can simply use the following:
```
SELECT DISTINCT year, product_type
FROM products
ORDER BY 1, 2;
```
This should give the following output:
![Distinct model years and product types!](images/mod.png)

Another keyword related to **DISTINCT** is **DISTINCT ON**. Now, **DISTINCT ON** allows you to ensure that only one row is returned, and one or more columns are always unique in the set. The general syntax of a **DISTINCT ON** query is as follows:
```
SELECT DISTINCT ON (distinct_column)
column_1,
column_2,
…
column_n
FROM table
ORDER BY order_column;
```
Here, **distinct_column** is the column(s) you want to be distinct in your query, **column_1** through **column_n** are the columns you want in the query, and **order_column** allows you to determine the first row that will be returned for a **DISTINCT ON** query if multiple columns have the same value for **distinct_column**.

For **order_column**, the first column mentioned should be **distinct_column**. If an **ORDER BY** clause is not specified, the first row will be decided randomly.

For example, you want to get a unique list of **salespeople** where each salesperson has a unique first name. In the case that two salespeople have the same first name, you will return the one that joined the company earlier. This query would look as follows:
```
SELECT DISTINCT ON (first_name)
   *
FROM
   salespeople
ORDER BY
   first_name, hire_date;
```
It should return this output:
![DISTINCT ON first_name!](images/dist.png)
This table now guarantees that every row has a distinct username. If there are multiple users with the same first name, then the user who was hired first by the company will be pulled by the query.

For example, if the **salespeople** table has multiple rows with the first name **Abby**, the row in the above Figure with the name of Abby (that is, the first row in the outputs) is for the first person employed at the company with the name Abby.

Likewise, when you have two employees with the same first name, the query results will order them by the start date. For example, when two
employees, Andrey Haack with the start date of 2016-01-10 and Andrey Kures with the start date of 2016-05-17, exist in the database, Andrey Haack will be listed first, since his start date is earlier.

## Building a Sales Model using SQL Techniques
You will clean and prepare the data for analysis using SQL techniques. 

The data science team wants to build a new model to help predict which customers are the best prospects for remarketing. A new data scientist has joined their team. It is your responsibility to help the new data
scientist prepare and build a dataset to be used to train a model. Write a query to assemble a dataset. 
Here are the steps to perform:
1. Open **pgAdmin**, connect to the **sqlda database**, and open the SQL query editor.
2. Use **INNER JOIN** to join the **customers** table to the **sales** table.
```
SELECT *
FROM sales s
JOIN customers c
ON s.customer_id = c.customer_id
```

3. Use **INNER JOIN** to join the **products** table to the **sales** table.
```
FROM sales s
JOIN customers c
ON s.customer_id = c.customer_id
JOIN products p
ON s.product_id = p.product_id
```

4. Use **LEFT JOIN** to join the **dealerships** table (right table) to the **sales** table (left table).
```
FROM sales s
LEFT JOIN dealerships d
ON d.dealership_id = s.dealership_id
JOIN customers c
ON s.customer_id = c.customer_id
JOIN products pON s.product_id = p.product_id
```

5. Return all columns of the **customers** table and the **products** table.
```
SELECT
c.*, p.*
FROM sales s
LEFT JOIN dealerships d
ON d.dealership_id = s.dealership_id
JOIN customers c
ON s.customer_id = c.customer_id
JOIN products p
ON s.product_id = p.product_id;
```


6. Return the **dealership_id** column from the **sales** table, but fill in **dealership_id** in **sales** with **-1** if it is **NULL**.
```
SELECT
COALESCE(s.dealership_id, -1) sales_dealership,
c.*, p.*
FROM sales s
LEFT JOIN dealerships d
ON d.dealership_id = s.dealership_id
JOIN customers c
ON s.customer_id = c.customer_id
JOIN products p
ON s.product_id = p.product_id;
```

7. Add a column called **high_savings** that returns **1** if the sales amount was **500** less than **base_msrp** or lower. Otherwise, it returns **0**. Please make sure that you perform the query on a joined table.
```
SELECT
COALESCE(s.dealership_id, -1) sales_dealership,
CASE
WHEN sales_amount < base_msrp - 500 THEN 1
ELSE 0
END high_savings,c.*, p.*
FROM sales s
LEFT JOIN dealerships d
ON d.dealership_id = s.dealership_id
JOIN customers c
ON s.customer_id = c.customer_id
JOIN products p
ON s.product_id = p.product_id;
```

**Expected Output:**
The following figure shows some of the rows from the output of this activity. You can see that a number of **dealership_id** are replaced with **-1** by the query, as they are indeed **NULL**. This is
because internet sales do not go through a dealership and thus do not have a **dealership_id** value. Some of the rows also have their value in the **high_savings** column marked as **1**, indicating the sales amount is $500 or more below **base_msrp**. You can go through some rows, try to get the original data, and confirm the SQL is written properly:
![Building a sales model query!](images/sal.png)



# Aggregate Functions for Data Analysis
You have learned how to use SQL to prepare datasets for analysis. Eventually, the purpose of data preparation is to make the data suitable for analysis so that you can make sense of it.

Once the data has been prepared, the next step is to analyze it. Generally, data scientists and analytics professionals will try to understand the data by summarizing it and trying to find high-level patterns.

SQL can help with this task primarily by using aggregate functions. These functions take multiple rows as input and return new information based on those input rows. 
To begin, you will learn about aggregate functions. In this text, you will understand the fundamentals of aggregate functions through the following topics:
- Aggregate Functions
- Aggregate Functions with the **GROUP BY** Clause
- Aggregate Functions with the **HAVING** Clause
- Using Aggregates to Clean Data and Examine Data Quality

## Aggregate Functions
In addition to just seeing individual rows of data, it is also interesting to understand the properties of an entire column or table. 

For example, say you just received a sample dataset of a fictional company called ZoomZoom, which specializes in car and electronic scooter retailing. You are wondering about the number of customers that this ZoomZoom database contains. You could select all the data from the
table and then see how many rows were pulled back, but it would be incredibly tedious to do so. Luckily, there are functions provided by SQL that can be used to perform this type of calculation on large groups of rows. These functions are called **aggregate functions**.

Aggregate functions take in one or more columns with multiple rows and return a number based on those columns. The following table provides a summary of the major aggregate functions that are used in SQL:
![Major aggregate functions!](images/aggregate.png)

The most frequently used aggregate functions include **SUM(), AVG(), MIN(), MAX(), COUNT(),** and **STDDEV()**.

Aggregate functions can help you to smoothly execute several tasks, such as the following:
- Aggregate functions can be used with the **WHERE** clause to calculate aggregate values for specific subsets of data. For example, if you want to know how many customers ZoomZoom has in California, you could use the following query:
```
SELECT
  COUNT(*)
FROM
  customers
WHERE
  state='CA';
  ```
This results in the following output:
![Result of COUNT(*) with the WHERE clause!](images/coun.png)

- You can do arithmetic with aggregate functions. In the following query, you can divide the count of rows in the **customers** table by 2:
```
SELECT
  COUNT(*)/2
FROM
  customers;
```
This query will return **25000**.
![Result of function – constant calculation!](images/2.png)

- You can use aggregate functions with each other in mathematical ways. If you want to calculate the average value of a specific column, you can use the **AVG** function. For example, to calculate the average **Manufacturer's Suggested Retail Price (MSRP)** of products at ZoomZoom, you can use the **AVG(base_msrp)** function in a query. In addition, you can also build the **AVG** function using **SUM** and **COUNT**, as follows:
```
SELECT
   SUM(base_msrp)/COUNT(*) AS avg_base_msrp
FROM
   Products;
```
You will get the following result:
![Result of function calculation!](images/res.png)

A frequently seen scenario is a calculation involving the **COUNT()** function. For example, you can use the **COUNT** function to count the total number of ZoomZoom customers by counting the total rows in the **customers** table:
```
SELECT
   COUNT(customer_id)
FROM
   customers;
```
The **COUNT** function will return the number of rows without a **NULL** value in the column. Since the **customer_id** column is a primary key and cannot be **NUL**L, the **COUNT** function will return the number of rows in the table. In this case, the query will return the following output:
![Result of the COUNT column!](images/co.png)

As shown here, the **COUNT** function works with a single column and counts how many non-**NULL** values it has. However, if the column has at least one **NULL** value, you will not be able to determine how many rows there are. To get a count of the number of rows in that situation, you could use the **COUNT** function with an asterisk in brackets, **(*)**, to get the total count of rows:
```
SELECT
   COUNT(*)
FROM
   customers;
```
This query will also return **50000**:
![Result of COUNT(*) as compared to the COUNT column!](images/co.png)

One of the major themes you will find in data analytics is that analysis is fundamentally only useful when there is a strong variation in the data. A column where every value is exactly the same is not a particularly useful column. To identify this potential issue, it often makes sense to determine how many distinct values there are in a column. To measure the number of distinct values in a column, you can use the **COUNT DISTINCT** function. The structure of such a query would look as follows:
```
SELECT
   COUNT (DISTINCT {column1})
FROM
   {table1}
```
Here, **{column1}** is the column you want to count and **{table1}** is the table with the column.

For example, say you want to verify that your customers are based in all 50 states of the US, possibly with the addition of Washington D.C., which is technically a federal territory but is treated as a state in
your system. For this, you need to know the number of unique states in the customer list. You can use **COUNT(DISTINCT expression)** to process the query:
```
SELECT
   COUNT(DISTINCT state)
FROM
   customers;
```
This query returns the following output:
![Result of COUNT DISTINCT!](images/di.png)

This result shows that you do have a national customer base in all 50 states and Washington D.C.. You can also calculate the average number of customers per state using the following SQL:
```
SELECT
   COUNT(customer_id)::numeric / COUNT(DISTINCT state)
FROM
   customers;
```
This query returns the following output:
![Result of COUNT division with casting!](images/divi.png)

1. Note that in the preceding SQL, the count of customer ID is cast as numeric. The reason you must cast this as numeric is that the **COUNT()** function always returns an integer. PostgreSQL treats integer division differently than float division in that it will ignore the decimal part of the result. For example, dividing 7 by 2 as integers in PostgreSQL will give you 3 instead of 3.5. In the preceding example, if you do not specify the casting, the SQL and its result will be as follows:
```
SELECT
   COUNT(customer_id) / COUNT(DISTINCT state)
FROM
   customers;
```
You will get this output:
![Result of COUNT division without casting!](images/cast.png)   

2. To get a more precise answer with a decimal part, you have to cast one of the numbers as a float. There is also an easier way to convert an integer into a float, which is to multiply it by 1.0. As 1.0 is a numeric value, its calculation with an integer value will result in a numeric value. For example, the following SQL will generate the same output as the SQL in the code block above;
![code block above!](images/divi.png)
```
SELECT
   COUNT(customer_id) * 1.0 / COUNT(DISTINCT state)
FROM
   customers;
```
### Using Aggregate Functions to Analyze Data
You will analyze and calculate the price of a product using different aggregate functions. For instance, say you are curious about the data at your company and interested in understanding some of the basic statistics around ZoomZoom product prices. Now, you want to calculate the lowest price, highest price, average price, and standard deviation of the price for all the products the company has ever sold.

1. Open **pgAdmin**, connect to the **sqlda** database, and open SQL query editor.
2. Calculate the lowest price, highest price, average price, and standard deviation of the price using the **MIN, MAX, AVG**, and **STDDEV** aggregate functions, respectively, from the **products** table:
```
SELECT
   MIN(base_msrp),
   MAX(base_msrp),
   AVG(base_msrp),
   STDDEV(base_msrp)
FROM
   products;
```
The preceding code will produce an output similar to this:
![Statistics of the product price!](images/avg.png)

From the preceding output, you can see that the minimum price is **349.99**, the maximum price is **115000.00**, the average price is **33358**.32750, and the standard deviation of the price is **44484.40866.**



## Aggregate Functions with the GROUP BY Clause
So far, you have used aggregate functions to calculate statistics for an entire column. However, most times you are interested in not only the aggregate values for a whole table but also the values for smaller groups in the table. To illustrate this, refer back to the **customers** table. You know that the total number of customers is 50,000. However, you might want to know how many customers there are in each state. But how can you calculate this?

You could determine how many states there are with the following query:
```
SELECT DISTINCT
   state
FROM
   customers;
```
You will see 50 distinct states, Washington D.C., and **NULL** returned as a result of the preceding query, totaling 52 rows. Once you have the list of states, you could then run the following query for each state:
```
SELECT
   COUNT(*)
FROM
   customers
WHERE
   state='{state}'
```
Although you can do this, it is incredibly tedious and can take a long time if there are many states. The **GROUP BY** clause provides a much more efficient solution.

### The GROUP BY Clause
**GROUP BY** is a clause that divides the rows of a dataset into multiple groups based on some sort of key that is specified in the clause. An aggregate function is then applied to all the rows within a single group to produce a single number for that group. The **GROUP BY** key and the aggregate value for the group are then displayed in the SQL output. The following diagram illustrates this general process:
![General GROUP BY computational model!](images/GROUP%20BY.png)

In the preceding diagram, you can see that the dataset has multiple groups **(Group 1, Group 2, …, Group N)**. Here, the aggregate function is applied to all the rows in **Group 1** and generates the result **Aggregate 1**. Then, the aggregate function is applied to all the rows in **Group 2** and generates the result **Aggregate 2**, and so on.

The **GROUP BY** statements usually have the following structure:
```
SELECT
   {KEY},
   {AGGFUNC(column1)}
FROM
   {table1}
GROUP BY
   {KEY}
```
Here, **{KEY}** is a column or a function on a column that is used to create individual groups. For each value of **{KEY}**, a group is created. **{AGGFUNC(column1)}** is an aggregate function on a column that is calculated for all the rows within each group. **{table}** is the table or set of joined tables from which rows are separated into groups.

To illustrate this point, you can count the number of customers in each US state using a **GROUP BY** query:
```
SELECT
   state, COUNT(*)
FROM
   customers
GROUP BY
   state;
```
The computational model looks like this:
![Customer count by the state computational model!](images/custo.png)
Here, **AK, AL, AR,** and the other keys are abbreviations for US states. This grouping is a two-step process. In the first step, SQL will create groups based on the existing states, one group for each state,
labeling the group with the state. SQL then will allocate customers into different groups based on their states. Once all the customers are allocated to their respective state groups, the execution goes into the
second step. In this step, SQL will apply the aggregate function to each group and associate the result with the group label, which is **state** in this case. The output of the SQL will be a set of aggregate function results with its state label. You should get the following output, in which **state** is the label and **count** is the aggregate result:
![Customer count by the state query output!](images/stat.png)

The **{KEY}** value for the **GROUP BY** operation can also be a function of column(s). The underlying example counts customers based on the year they were added to the database. Here, the year was the result of the **TO_CHAR** function on the **date_added** column:
```
SELECT
  TO_CHAR(date_added, 'YYYY'),
  COUNT(*)
FROM
  customers
GROUP BY
  TO_CHAR(date_added, 'YYYY')
ORDER BY 1;
```
The result of this SQL is as follows:
![Customer count GROUP BY function!](images/tochar.png)

You can also use the column number to perform a **GROUP BY** operation:
```
SELECT
   state,
   COUNT(*)
FROM
   customers
GROUP BY 1;
```
This SQL will return the same result as the previous one, which used the column name in the **GROUP BY** clause.

If you want to return the output in alphabetical order, simply use the following query:
```
SELECT
  state,
  COUNT(*)
FROM
  customers
GROUP BY
  state
ORDER BY
  state;
```
Alternatively, you can write the following with the column order number in **GROUP BY** and **ORDER BY** instead of column names:
```
SELECT
   state,
   COUNT(*)
FROM
   customers
GROUP BY
   1
ORDER BY 1;
```
Either of these queries will give you the following result:
![Customer count by the state query output in alphabetical order!](images/outp.png)

Often, though, you may be interested in ordering the aggregates themselves. You may want to know the number of customers in each state in increasing order so that you know which state has the least number of customers. You can then use this result to make a business decision, such as launching a new marketing campaign in the states where you don't have enough presence. This would require you to order the aggregates themselves. The aggregates can also be ordered using **ORDER BY**, as follows:
```
SELECT
   state,
   COUNT(*)
FROM
   customers
GROUP BY
   state
ORDER BY
   COUNT(*);
```
This query gives you the following output:
![Customer count by the state query output in increasing order!](images/order.png)

You may also want to count only a subset of the data, such as the total number of male customers in a particular state. To calculate the total number of male customers, you can use the following query:
```
SELECT
   state, COUNT(*)
FROM
   customers
WHERE
   gender='M'
GROUP BY
   state
ORDER BY
   State;
```
This gives you the following output:
![Male customer count by the state query output in alphabetical order!](images/male.png)

As shown here, grouping by one column can provide some great insight. You can get different aspects of the entire dataset, as well as any subset that you may think of. You can use these characteristics to
construct a hypothesis and try to verify it. For example, you can identify the sales and the count of customers in each state, or better yet, the count of a specific subgroup of customers. From there, you
can run a bivariate analysis,If you can find a relationship between the sales amount and the particular group of customers, you may be able to figure out some way to reach out to more of these customers and thus increase the sales, or to figure out why other groups of customers are not as motivated.

### Multiple-Column GROUP BY
While **GROUP BY** with one column is helpful, you can go even further and use **GROUP BY** on multiple columns. For instance, say you wanted to get a count of not just the number of customers ZoomZoom had in each state but also how many male and female customers it had in each state. You can find this using multiple **GROUP BY** columns, as follows:
```
SELECT
  state, gender, COUNT(*)
FROM
  customers
GROUP BY
  state, gender
ORDER BY
  state, gender;
```
This gives you the following result:
![Customer count by the state and gender query outputs in alphabetical order!](images/alph.png)

Any number of columns can be used in a **GROUP BY** operation in the same way as illustrated in the preceding example. In this case, SQL will create one group for each unique combination of column values, such as one group for **state=AK** and **gender=F**, another for **state=AK**, and **gender=M**, and so on, then calculate the aggregate function for each group and label the result with a value from all the grouping columns.

### Calculating the Cost by Product Type Using GROUP BY
You will analyze and calculate the cost of products using aggregate functions and the **GROUP BY** clause. The marketing manager wants to know the minimum, maximum, average, and standard deviation of the price for each product type that ZoomZoom sells for a marketing campaign.
1. Open **pgAdmin**, connect to the **sqlda** database, and open SQL query editor.
2. Calculate the lowest price, highest price, average price, and standard deviation of the price using the **MIN, MAX, AVG,** and **STDDEV** aggregate functions from the products table and use
**GROUP BY** to check the price of all the different product types:
```
SELECT
   product_type,
   MIN(base_msrp),
   MAX(base_msrp),
   AVG(base_msrp),
   STDDEV(base_msrp)
FROM
   products
GROUP BY
   1
ORDER BY 1;
```
You should get the following result:
![Basic price statistics by product type!](images/basic.png)



## Grouping Sets
It is very common to want to see the statistical characteristics of a dataset from several different perspectives. For instance, say you wanted to count the total number of customers you have in each state, while simultaneously, you also wanted the total number of male and female customers you have in each state. One way you could accomplish this is by using the **UNION ALL** keyword.
```
(
SELECT
   state,
   NULL as gender,
   COUNT(*)
FROM
   customers
GROUP BY
   1, 2
ORDER BY
   1, 2
)
UNION ALL
(
SELECT
   state,
   gender,
   COUNT(*)
FROM
   customers
GROUP BY
   1, 2
ORDER BY
   1, 2
)
ORDER BY 1, 2;
```
This query produces the following result:
![Customer count by the state and gender query outputs in alphabetical order!](images/UNI.png)
Fundamentally, what you are doing here is creating multiple sets of aggregation, one grouped by state and another grouped by state and gender, and then joining them together. Thus, this operation is called grouping sets, which means multiple sets are generated using GROUP BY. However, using **UNION ALL** is tedious and can involve writing lengthy queries. An alternative way to do this is to use the **GROUPING SETS** statement. This statement allows a user to create multiple sets of grouping for viewing, similar to the **UNION ALL** statement. For example, using the **GROUPING SETS** keyword, you could rewrite the previous **UNION ALL** query, like so:
```
SELECT
   state,
   gender,
   COUNT(*)
FROM
   customers
GROUP BY GROUPING SETS (
  (state),
  (state, gender)
)
ORDER BY
1, 2;
```
This creates the same output as the previous **UNION ALL** query.

### Ordered Set Aggregates
You can order the data using **ORDER BY**, but this is not required to
complete the calculation, nor will the order impact the result. However, there is a subset of aggregate statistics that depends on the order of the column to calculate. For instance, the median of a column is something that requires the order of the data to be specified. To calculate these use cases, SQL offers a series of functions called **ordered set aggregate** functions. The following table lists the main ordered set aggregate functions:
![Major ordered set aggregate functions!](images/set.png)

These functions are used in the following format:
```
SELECT
   {ordered_set_function} WITHIN GROUP (ORDER BY {order_column})
FROM {table};
```
Here, **{ordered_set_function}** is the ordered set aggregate function, **{order_column}** is the column to order results for the function by, and **{table}** is the table the column is in. For example, you can calculate the median price of the **products** table by using the following query:
```
SELECT
   PERCENTILE_CONT(0.5)
   WITHIN GROUP (ORDER BY base_msrp)
   AS median
FROM
   products;
```
The reason you use **0.5** is that the median is the 50th percentile, which is 0.5 as a fraction. This gives you the following result:
![Result of an ordered set aggregate function!](images/perc.png)

## Aggregate Functions with the HAVING Clause
**GROUP BY** is a two-step process. In the first step, SQL selects rows from the original table or table set to form aggregate groups. In the second step, SQL calculates the aggregate function results. When you apply a **WHERE** clause, its conditions are applied to the original table or table set, which means it will always be applied in the first step. Sometimes, you are only interested in certain rows in the aggregate function result with certain characteristics, and only want to keep them in the query output and remove the rest. This can only happen after the aggregation has been completed and you get the results, thus it is part of the second step of **GROUP BY** processing. For example, when doing the customer counts, perhaps you are only interested in places that have at least 1,000 customers. Your first instinct may be to write something such as this:
```
SELECT
  state, COUNT(*)
FROM
  customers
WHERE
  COUNT(*)>=1000
GROUP BY
  state
ORDER BY
  state;
```
However, you will find that the query does not work and gives you the following error:
![Error showing the query is not working!](images/errr.png)

This is because **COUNT(*)** is calculated at the second step on the aggregated groups. Thus, this filter can only be applied to the aggregated groups, not the original dataset. So, using the **WHERE** clause on aggregate functions will produce an error. To use the filter on aggregate functions, you need to use a new clause: **HAVING**. The **HAVING** clause is similar to the **WHERE** clause, except it is specifically designed for **GROUP BY** queries. It applies the filter condition on the aggregated groups instead of the original dataset. The general structure of a **GROUP BY** operation with a **HAVING** statement is as follows:
```
SELECT
   {KEY},
   {AGGFUNC(column1)}
FROM
   {table1}
GROUP BY
   {KEY}
HAVING
   {OTHER_AGGFUNC(column2)_CONDITION}
```

Here, **{KEY}** is a column or a function on a column that is used to create individual groups, **{AGGFUNC(column1)}** is an aggregate function on a column that is calculated for all the rows within each group, **{table}** is the table or set of joined tables from which rows are separated into groups, and **{OTHER_AGGFUNC(column2)_CONDITION}** is a condition similar to what you would put in a **WHERE** clause involving an aggregate function. 

### Calcualting and Displaying Data using the HAVING Clause
You will calculate and display data using the **HAVING** clause. The sales manager of ZoomZoom wants to know the customer count for the states that have at least 1,000 customers who have purchased any product from ZoomZoom. Perform the following steps to help the manager to
extract the data:
1. Open **pgAdmin**, connect to the **sqlda** database, and open SQL query editor.
2. Calculate the customer count by states with at least **1000** customers using the **HAVING** clause:
```
SELECT
   state, COUNT(*)
FROM
   customers
GROUP BY
   state
HAVING
   COUNT(*)>=1000
ORDER BY
   state;
```
This query will give you the following output:
![Customer count by states with at least 1,000 customers!](images/hav.png)

Here, you can see the states that have more than 1,000 ZoomZoom customers, with **CA** having **5038**, the highest number of customers, and **CO** having **1042**, the lowest number of customers.



## Using Aggregates to Clean Data and Examine Data Quality
Aggregates add a number of techniques that can make cleaning data easier and more comprehensive.

### Finding Missing Values with GROUP BY
Using aggregates, identifying the amount of missing data can tell you not only which columns have missing data but also the usability of the columns when so much of the data is missing. Depending on the extent of missing data, you will have to determine whether it makes sense to delete rows with missing data, fill in missing values, or just delete columns if they do not have enough data to make definitive conclusions.

The easiest way to determine whether a column is missing values is to use a modified **CASE WHEN** statement, which provides flexible logic to check whether a condition is met, with the **SUM** and **COUNT** functions to determine what percentage of data is missing. The query looks as follows:
```
SELECT
   SUM(
CASE
   WHEN
      {column1} IS NULL
        OR
      {column1} IN ({missing_values})
        THEN 1
        ELSE 0
END
   )::FLOAT/COUNT(*)
FROM
   {table1}
```
Here, **{column1}** is the column that you want to check for missing values, **{missing_values}** is a comma-separated list of values that are considered missing, and **{table1}** is the table or subquery with the missing values.

Based on the results of this query, you may have to vary your strategy for dealing with missing data. If a very small percentage of your data is missing (<1%), then you might consider just filtering out or deleting the missing data from your analysis. If some of your data is missing (<20%), you may consider filling in your missing data with a typical value, such as the mean or the mode, to perform an accurate analysis. If more than 20% of your data is missing, you may have to remove the column from your data analysis, as there would not be enough data to make accurate conclusions based on the values in the column.

Now look at missing data in the **customers** table. Specifically, look at the missing data in the **state** column. Based on some prior knowledge, the business team has determined that if the **state** column in a row contains **NULL** or is an empty string (''), this value is
considered a missing value. You now need to determine the extent of missing values to see whether this **state** column is still useful. You will do so by dividing the number of records that have the missing value in the **state** column by the total number of the records:
```
SELECT
   SUM(
CASE
   WHEN state IS NULL OR state IN ('') THEN 1
      ELSE 0
END
   )::FLOAT/COUNT(*) AS missing_state
FROM
   customers;
```
This gives you the following output:
![Result of NULL and missing value percentage calculation!](images/nul.png)
As shown here, a little under 11% of the state data is missing. For analysis purposes, you may want to consider that these customers are from California, since **CA** is the most common state in the data.
However, the far more accurate thing to do would be to find and fill in the missing data.

If you are only concerned about **NULL** values, and there is no need to check other missing values, you can also use a **COUNT()** function, which counts from the column. Such a **COUNT()** function will
only count the non-**NULL** values. By dividing this value by the total count, you will get the percentage of non-**NULL** values. By subtracting non-NULL percentage from 100%, you will get the percentage of
**NULL** values in the total count:
```
SELECT
   COUNT(state) * 1.0 / COUNT(*) AS non_null_state,
   1 - COUNT(state) * 1.0 / COUNT(*) AS null_state
FROM
   customers;
```
This gives you the following output of the percentages of non-**NULL** and **NULL** values displayed as fractions:
![Result of NULL value percentage calculation!](images/re.png)
You can see that the **null_state*** value here is the same as the **missing_state** value in the previous SQL. This shows that there is actually no value with an empty string (''). All missing values are **NULL**.

### Measuring Data Uniqueness with Aggregates
Another common task that you might want to perform is to determine whether every value in a column is unique. While in many cases this can be solved by setting a column with a **PRIMARY KEY** constraint, this may not always be possible. To solve this problem, you can write the following query:
```
SELECT
   COUNT (DISTINCT {column1})=COUNT(*)
FROM
   {table1}
```
Here, **{column1}** is the column you want to count and **{table1}** is the table with the column. If this query returns **True**, then the column has a unique value for every single row; otherwise, at least
one of the values is repeated. If values are repeated in a column that you are expecting to be unique, there may be some issues with the data **Extract, Transform, and Load (ETL)** or there may be a join that has caused a row to be repeated.

As a simple example, verify that the **customer_id** column in **customers** is unique:
```
SELECT
   COUNT(DISTINCT customer_id)=COUNT(*) AS equal_ids
FROM
   customers;
```
This query gives you the following output, which shows that the values in the **customer_id** column are truly unique:
![Result of comparing COUNT DISTINCT versus COUNT(*)!](images/cou.png)

### Analyzing Sales Data Using Aggregate Functions
You will analyze data using aggregate functions. The CEO, COO, and CFO of
ZoomZoom would like to gain some insight into the common statistical characteristics of sales now that the company feels they have a strong enough analytics team with your arrival. The task has been given to you, and your boss has politely let you know that this is the most important project the analytics team has worked on. Perform the following steps to complete this activity:
1. Open **pgAdmin**, connect to the **sqlda** database, and open SQL query editor.
2. Calculate the total number of unit sales the company has made.
```
SELECT
   COUNT(*)
FROM
   sales;
```
The result is as follows:
![Result of COUNT(*) for sales units!](images/sales%20count.png)
Note that because each sales transaction contains a product ID, there is no **NULL** value in the **product_id** column. So, **COUNT(product_id)** will also work. Similarly, **COUNT(sales_amount)** will also work.

3. Calculate the total sales amount in dollars for each state.
```
SELECT
c.state,
SUM(s.sales_amount)::DECIMAL(12,2)
FROM
sales s
JOIN
customers c
ON
s.customer_id = c.customer_id
GROUP BY
c.state
ORDER BY
1;
```
The result is as follows:
![Result of sales by state!](images/state%20sales.png)   

4. Identify the top five best dealerships in terms of the most units sold (ignore internet sales).
The most common approach to getting the top/bottom **N** rows is to run the **SELECT** statement with **ORDER BY**, then use **LIMIT** to only get the first **N** rows. In this activity, you can use **LIMIT 5**
together with **ORDER BY DESC** to generate the top five dealerships. However, if there is a tie between the 5th and sixth elements, **LIMIT 5** will cut off between the 5th row and sixth row, regardless of whether you want both items or not. In the real world, you need to check the boundary condition carefully, that is, check the value below the limit to make sure there is no tie.

For this question, if you just aim at getting the dealership ID, the following SQL is good enough. However, if you would like to have the dealership details, you need to select the information from the
dealerships table, with a filter on the dealership IDs from the following query:
```
SELECT
s.dealership_id,
COUNT(*)
FROM
sales s
WHERE
channel <> 'internet'
GROUP BY
s.dealership_id
ORDER BY
2 DESC
LIMIT
5;
```
Here is the output:
![Result of top five dealerships by sales!](images/sales%20dealership.png)

5. Calculate the average sales amount for each channel, as shown in the sales table, and look at the average sales amount, first by **channel** sales, then by **product_id**, and then both together.
```
SELECT
channel,product_id,
AVG(sales_amount)
FROM
sales
GROUP BY grouping sets (
(channel),
(product_id),
(channel, product_id)
);
```
The result is as follows. Note that in this screenshot (the order of rows in your result may vary), row 22 and above are grouped by both **channel** and **product_id**. Rows 23 and 24 are grouped by
**channel** only, and row 25 and beyond are grouped by **product_id** only. In other words, there are three different sets here, one is grouped by both **channel** and **product_id**, the other two by one
of these two columns respectively, and all three sets are eventually joined together:
![Result of GROUPING SETS!](images/sets.png)

**Expected Output**
![Sales after the GROUPING SETS channel and product_id!](images/group.png)

1. Calculate the percentage of sales transactions that have a **NULL** dealership.
```
SELECT
   COUNT(dealership_id) * 1.0 / COUNT(*) AS non_null_dealership,
   1 - COUNT(dealership_id) * 1.0 / COUNT(*) AS null_dealership
FROM
sales
```
The result is as follows:
![Ratio of NULL values of dealership in sales!](images/null%20dealership.jpg)

2. Calculate the percentage of internet sales the company has made for each year. Order the year in a timely fashion and you will get time series data. Does this time series suggest something?
```
SELECT
TO_CHAR(sales_transaction_date, 'yyyy'),
SUM(sales_amount)
FROM
sales
WHERE
channel = 'internet'
GROUP BY
1
ORDER BY
1;
```
The result is as follows:
![Internet sales by year!](images/internetsales.png)

From the result data, you can see that there was a significant increase in sales starting in 2015. The upward trend is continuing into 2022, which is still at the beginning of the year at the point of data
collection (the last sales transaction date is 2022-01-25). But does this increase occur in the overall sales of ZoomZoom, or does it only happen to the internet sales channel? If it is the former, internet
sales and non-internet sales should have a similar amount of increase. There are many ways to measure and compare these two increases. You will use the simplest form by listing the internet sales and non-internet sales side by side. The SQL will be as follows:
```
SELECT
TO_CHAR(sales_transaction_date, 'yyyy'),
SUM(
CASE
WHEN channel = 'internet' THEN sales_amount
ELSE 0
END
) AS internet_sales,
SUM(
CASE
WHEN channel <> 'internet' THEN sales_amount
ELSE 0
END
) AS non_internet_sales
FROM
sales
GROUP BY
1
ORDER BY
1;
```
The result is as follows:
![Internet and non-internet sales by year!](images/int%20sales.png)

**CASE**, **NULLIF**, and **COALESCE**, are applied to one data row and will generate one output value for each row in the raw data. The aggregate functions, such as **COUNT** and **SUM**, are applied to a dataset of many rows and will generate one output value for the entire dataset. The former can be used to analyze the characteristics of a data point, while the latter can be used to analyze the statistics of a dataset.



# Window Functions for Data Analysis





































