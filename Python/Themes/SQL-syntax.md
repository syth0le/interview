# Junior-level![img.png](img.png)
**SELECT**

```sql 
SELECT city FROM Customers;
```

DISTINCT

```sql 
SELECT DISTINCT Country FROM Customers;
```

WHERE

```sql
SELECT * FROM Customers WHERE City = 'Berlin';
```

NOT

```sql
SELECT * FROM Customers WHERE NOT City = 'Berlin';
```

AND

```sql
SELECT * FROM Customers WHERE NOT City = 'Berlin' AND PostalCode = 199373;
```

OR

```sql
SELECT * FROM Customers WHERE NOT City = 'Berlin' OR City = 'DONBASS';
```

ORDER BY = ASC(В алфавитном порядке и по возрастанию по умолчанию)

Сортировка по одному полю:
```sql
SELECT * FROM Customers ORDER BY City;
```

Сортировка по нескольким полям сразу:
```sql
SELECT * FROM Customers ORDER BY Country, City;
```

DESC (В обратном алфавитном порядке и по убыванию)

```sql
SELECT * FROM Customers ORDER BY City;
```

ORDER BY (В алфавитном порядке и по возрастанию по умолчанию)

```sql
SELECT * FROM Customers ORDER BY City;
```

INSERT

```sql

INSERT INTO Customers (CustomerName, Address, City, PostalCode,Country)
VALUES ('Hekkan Burger','Gateveien 15','Sandnes','4306','Norway');
```

NULL

```sql
SELECT * FROM Customers WHERE PostalCode IS NOT NULL;
```

MIN

```sql
SELECT MIN(Price) FROM Products;
```

MAX

```sql
SELECT MAX(Price) FROM Products;
```

COUNT

```sql
SELECT COUNT(City) FROM Customers;
```

```sql
SELECT COUNT(*) FROM Products WHERE Price = 18;
```

AVG

```sql
SELECT AVG(Price) FROM Products;
```

SUM

```sql
SELECT SUM(Price) FROM Products;
```

UPDATE

```sql
UPDATE Customers SET City = 'Oslo';
```

```sql
UPDATE Customers SET City = 'Oslo', Country = 'Norway' WHERE CustomerID = 32;
```

DELETE

Удаляет конкретную запись:
```sql
DELETE FROM Customers WHERE Country = 'Norway';
```
Удаляет все записи в таблице:
```sql
DELETE FROM Customers;
```

LIKE

Выберите все записи, в которых значение столбца City начинается с буквы "а":
```sql
SELECT * FROM Customers WHERE City LIKE 'a%';
```
Заканчивается на "a":
```sql
SELECT * FROM Customers WHERE City LIKE 'a%';
```
Содержит "a":
```sql
SELECT * FROM Customers WHERE City LIKE '%a%';
```
Начинается с "а" и заканчивается на "б":
```sql
SELECT * FROM Customers WHERE City LIKE 'a%б';
```
НЕ начинаются с "а":
```sql
SELECT * FROM Customers WHERE City NOT LIKE 'a%';
```

# TODO: ОПЕРАТОРЫ КАК В REGEXP сюда вставить

https://www.schoolsw3.com/sql/exercise_in1.php
in
between
join
group by
подстановочный знак
as



LIMIT

JOIN(ALL KINDS) +-


# Middle-level

AGGREGATION FUNCTIONS

HAVING

DELETE

DIFFERENCE BETWEEN RELATION DBs AND NoSQL

ACID

TRANSACTIONS AND PROBLEMS OF TRANSACTIONS

INDEX

AWARE OF DB SCHEMA

RELATIONS (ALL KINDS)

DATA UPDATE ON MIGRATIONS

WINDOW FUNCTIONS