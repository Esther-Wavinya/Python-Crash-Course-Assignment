
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














