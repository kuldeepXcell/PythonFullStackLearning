USE UpdateDB;

DESCRIBE computer;
CREATE PROCEDURE select_all()
SELECT * FROM computer;

CALL select_all();
CALL sample();

DELIMITER $$
CREATE PROCEDURE all_data2(brand VARCHAR(50))
BEGIN
	SELECT * FROM computer 
    WHERE c_brand = brand;
END$$	
DELIMITER ;
CALL all_data1();
DELIMITER $$
CREATE PROCEDURE samsung_product()
BEGIN
	SELECT * FROM product
    WHERE p_name LIKE '%Samsung%';
END$$
DELIMITER ;

CALL samsung_product();

CALL all_data2('HP');
