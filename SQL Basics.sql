CREATE DATABASE homework1;
USE homework1;

CREATE TABLE product(
id INT,
p_name VARCHAR(20),
p_price DECIMAL(4,2)
);

CREATE TABLE people(
id INT,
p_name VARCHAR(20),
p_phone_number VARCHAR(10),
p_DOB DATE,
p_height DECIMAL(3,2)
);

CREATE TABLE computer(
brand VARCHAR(10),
ram INT, 
processor VARCHAR(20),
price INT
);
SHOW TABLES;

CREATE TABLE person(
id INT,
p_name VARCHAR(25)
);

describe person;

ALTER TABLE person
ADD age INT;

ALTER TABLE person
DROP COLUMN age;
SELECT * FROM person;

