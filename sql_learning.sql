CREATE DATABASE sql_learning;
USE sql_learning;

CREATE TABLE emp(
eid INT PRIMARY KEY,
first_name VARCHAR(20) NOT NULL,
last_name VARCHAR(20) NOT NULL,
salary INT NOT NULL
);

INSERT INTO emp values
(1,'Kuldeep','Modh',50000),
(2,'Arjun','Modh',100000),
(3,'Karan','Modi',150000),
(4,'ABC','XYZ',25000),
(5,'QWERTY','A',10000);

SELECT * from emp;

-- A simple Stored Procedure
DELIMITER $$
CREATE PROCEDURE salary_more_than(_salary INT)
BEGIN
	SELECT * FROM emp WHERE SALARY > _salary;
END$$
DELIMITER ;

CALL salary_more_than(25000);

-- Stored Procedure for Handling Error when Calling the Procedure
DROP PROCEDURE IF EXISTS salary_hike;
DELIMITER $$
CREATE PROCEDURE salary_hike(
IN _empid INT,
IN _percentage INT)
BEGIN
	-- Error raised if occured during UPDATE Statement's Execution
	DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
    BEGIN
		SELECT CONCAT('Error : EMployee id ',_empid,'Doesnot Exist !') AS ErrorMessage;
    END;
	UPDATE emp SET salary = salary + (salary * _percentage / 100) WHERE eid = _empid;
	IF ROW_COUNT() > 0 THEN
        SELECT 'Salary updated successfully.' AS SuccessMessage;
    ELSE
		-- ErrorMessage Will be shown for the SELECT Statement
        SELECT CONCAT('Error: Employee ID ', _empid, ' does not exist or salary update failed.') AS ErrorMessage;
    END IF;
END$$
DELIMITER ;

SELECT * FROM emp;

CALL salary_hike(2,20);
CALL salary_hike(10,50);

-- Stored Procedure with IN and OUT parameters
DROP PROCEDURE IF EXISTS get_employee_name;
DELIMITER $$
CREATE PROCEDURE get_employee_name(
    IN emp_id INT,
    OUT emp_name VARCHAR(100)
)
BEGIN
    SELECT CONCAT(first_name,' ',last_name) INTO emp_name FROM emp WHERE eid = emp_id;
END$$
DELIMITER ;
SET @f_name = '';
CALL get_employee_name(3,@f_name);
SELECT @f_name AS Employee_Name;

-- Triggers in SQL

CREATE TABLE emp_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_id INT,
    old_salary DECIMAL(10, 2),
    new_salary DECIMAL(10, 2),
    change_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
-- Trigger to maintain an Audit Table For Inserting new Employee
DROP TRIGGER IF EXISTS after_change;
DELIMITER $$
CREATE TRIGGER after_change
AFTER INSERT ON emp
FOR EACH ROW
BEGIN
	INSERT INTO emp_audit VALUES (DEFAULT,NEW.eid,0,NEW.salary,DEFAULT);
END$$
DELIMITER ;

-- Trigger to maintain an Audit Table For Updation in Salary of Employee
Delimiter $$
CREATE TRIGGER after_update
AFTER UPDATE ON emp
FOR EACH ROW
BEGIN
	INSERT INTO emp_audit VALUES (DEFAULT,OLD.eid,OLD.salary,NEW.salary,DEFAULT);
END$$
DELIMITER ;

-- Trigger to maintain an Audit Table For Deletion of Employee
CREATE TABLE emp_deletion_log(
id INT PRIMARY KEY AUTO_INCREMENT,
emp_name VARCHAR(40) NOT NULL,
emp_del_date DATETIME DEFAULT CURRENT_TIMESTAMP);

Delimiter $$
CREATE TRIGGER emp_deletion
AFTER DELETE ON emp
FOR EACH ROW
BEGIN
	INSERT INTO emp_deletion_log VALUES (DEFAULT,CONCAT(OLD.first_name,' ',OLD.last_name),DEFAULT);
END$$
DELIMITER ;

INSERT INTO emp VALUES (9,'SMS','DMS',20000);
UPDATE emp SET salary = salary + 500;
DELETE FROM emp WHERE eid = 6;

SELECT * FROM emp;
SELECT * FROM emp_audit;
SELECT * FROM emp_deletion_log;

DROP FUNCTION IF EXISTS bonus_calculator;
DELIMITER $$
CREATE FUNCTION bonus_calculator(_salary INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE temp INT;
	SET temp = _salary;
	RETURN temp*0.1255;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE sample(_salary INT)
BEGIN
	SELECT salary,bonus_calculator(salary) FROM emp ;
END$$
DELIMITER ;
CALL sample(25000);

DELIMITER $$
CREATE TRIGGER total_pay
AFTER UPDATE on emp
FOR EACH ROW
BEGIN
	UPDATE sample SET total_pay = total_pay + bonus;
END$$
DELIMITER ;


SELECT emp.*,bonus_calculator(salary) AS Bonus,(salary + bonus_calculator(salary)) AS Total_Pay FROM emp;