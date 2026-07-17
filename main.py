# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
df_boston = pd.read_sql("SELECT firstName, lastName FROM employees JOIN offices USING(officeCode) WHERE city = 'Boston'", conn)

# STEP 2
df_zero_emp = pd.read_sql("SELECT * FROM offices LEFT JOIN employees USING(officeCode) WHERE employeeNumber IS NULL", conn)

# STEP 3
df_employee = pd.read_sql("SELECT firstName, lastName, city, state FROM employees LEFT JOIN offices USING(officeCode) ORDER BY firstName, lastName", conn)

# STEP 4
df_contacts = pd.read_sql("SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber FROM customers LEFT JOIN orders USING(customerNumber) WHERE orderNumber IS NULL ORDER BY contactLastName", conn)

# STEP 5
df_payment = pd.read_sql("SELECT contactFirstName, contactLastName, amount, paymentDate FROM customers JOIN payments USING(customerNumber) ORDER BY CAST(amount AS REAL) DESC", conn)

# STEP 6
df_credit = pd.read_sql("SELECT employeeNumber, firstName, lastName, COUNT(customerNumber) AS num_customers FROM employees JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber GROUP BY employeeNumber HAVING AVG(creditLimit) > 90000 ORDER BY num_customers DESC", conn)

# STEP 7
df_product_sold = pd.read_sql("SELECT productName, COUNT(orderNumber) AS numorders, SUM(quantityOrdered) AS totalunits FROM products JOIN orderdetails USING(productCode) GROUP BY productCode ORDER BY totalunits DESC", conn)

# STEP 8
df_total_customers = pd.read_sql("SELECT productName, productCode, COUNT(DISTINCT customerNumber) AS numpurchasers FROM products JOIN orderdetails USING(productCode) JOIN orders USING(orderNumber) GROUP BY productCode ORDER BY numpurchasers DESC", conn)

# STEP 9
df_customers = pd.read_sql("SELECT COUNT(customerNumber) AS n_customers, officeCode, offices.city AS city FROM offices JOIN employees USING(officeCode) JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber GROUP BY officeCode", conn)

# STEP 10
df_under_20 = pd.read_sql("SELECT DISTINCT employeeNumber, firstName, lastName, offices.city AS city, officeCode FROM employees JOIN offices USING(officeCode) JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber JOIN orders USING(customerNumber) JOIN orderdetails USING(orderNumber) WHERE productCode IN (SELECT productCode FROM orderdetails JOIN orders USING(orderNumber) GROUP BY productCode HAVING COUNT(DISTINCT customerNumber) < 20) ORDER BY lastName", conn)

conn.close()