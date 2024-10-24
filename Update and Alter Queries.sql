CREATE DATABASE UpdateDB;
USE UpdateDB;

CREATE TABLE product(
id INT PRIMARY KEY,
p_name VARCHAR(30),
p_price INT
);

ALTER TABLE product
MODIFY COLUMN id INT AUTO_INCREMENT;

DESCRIBE product;

INSERT INTO product (p_name,p_price) VALUES ('Samsung Mobile',5000);
INSERT INTO product (p_name,p_price) VALUES ('Iphone',50000);
INSERT INTO product (p_name,p_price) VALUES ('Motorola Mobile',10000);
INSERT INTO product (p_name,p_price) VALUES ('Samsung TV',5000);
INSERT INTO product (p_name,p_price) VALUES ('Samsung Display',8000);

SELECT * FROM product;

UPDATE product SET p_price = 100000 WHERE p_name LIKE 'Samsung%';

CREATE TABLE people(
id INT PRIMARY KEY AUTO_INCREMENT,
p_name VARCHAR(20),
p_profession VARCHAR(20)
);

INSERT INTO people VALUES(DEFAULT,'Kuldeep','Engineer');
INSERT INTO people VALUES(DEFAULT,'Kuldeep','Doctor');
INSERT INTO people VALUES(DEFAULT,'DEF','Musician');
INSERT INTO people VALUES(DEFAULT,'ABC','Dancer');
INSERT INTO people VALUES(DEFAULT,'Arjun','Soldier');

SELECT * FROM people;

UPDATE people SET p_profession = 'Commander' WHERE p_name = 'Arjun';

CREATE TABLE computer(
c_brand VARCHAR(20), 
c_name VARCHAR(20),
c_processor VARCHAR(10)
);

ALTER TABLE computer
RENAME COLUMN c_name TO c_ram;

SELECT * FROm computer;
DESCRIBE computer;

ALTER TABLE computer
MODIFY COLUMN c_ram INT;

INSERT INTO computer VALUES ('HP',8,'i9');
INSERT INTO computer VALUES ('Samsung',16,'intel i9');
INSERT INTO computer VALUES ('Asus',16,'Ryzen 9');
INSERT INTO computer VALUES ('Apple',24,'M1');
INSERT INTO computer VALUES ('Asus',12,'Ryzen 7');

Update computer SET c_ram = 024 WHERE c_brand IN ('Samsung','Asus','Apple');
