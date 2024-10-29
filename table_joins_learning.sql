USE sql_learning;

CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

INSERT INTO departments (department_name) VALUES 
('Human Resources'), 
('IT'), 
('Sales'), 
('Marketing');

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INT,
    salary DECIMAL(10, 2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO employees (first_name, last_name, department_id, salary) VALUES 
('Alice', 'Smith', 1, 60000), 
('Bob', 'Johnson', 2, 80000), 
('Charlie', 'Williams', 2, 65000), 
('David', 'Brown', 3, 50000), 
('Eve', 'Davis', 4, 55000);

CREATE TABLE projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    employee_id INT,
    start_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO projects (project_name, employee_id, start_date) VALUES 
('Project Lambda', 1, '2023-02-28'),
('Project Alpha', 1, '2023-01-15'), 
('Project Beta', 2, '2023-02-10'), 
('Project Gamma', 3, '2023-03-05'), 
('Project Delta', 4, '2023-04-20');

-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : Retrieve a list of all employees along with their department names. 
-- The result should include the employee's first name, last name, and department name.

SELECT 
    e.first_name, e.last_name, d.department_name
FROM
    employees e
        INNER JOIN
    departments d ON e.department_id = d.department_id;
-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : Get a list of employees who are currently assigned to projects.
-- Include the employee's first name, last name, project name, and start date.

SELECT 
    CONCAT(e.first_name, e.last_name) Full_Name,
    p.project_name,
    p.start_date
FROM
    employees e
        INNER JOIN
    projects p ON e.employee_id = p.employee_id;     

-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : Generate a report that counts the number of employees in each department. 
-- The result should display the department name and the number of employees.

SELECT 
    d.department_name, COUNT(e.employee_id) 'No of Employees'
FROM
    departments d
        INNER JOIN
    employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : Retrieve a list of projects along with the corresponding employee's first and last names and their department names.
-- Include project name, employee name, and department name in the output.

SELECT 
    p.project_name,
    CONCAT(e.first_name, ' ', e.last_name) 'Employee Name',
    d.department_name
FROM
    projects p
        INNER JOIN
    employees e ON p.employee_id = e.employee_id
        INNER JOIN
    departments d ON d.department_id = e.department_id;
-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : Find all employees who work in the IT department and have a salary greater than $70,000.
-- Return their first name, last name, and salary.

SELECT 
    CONCAT(e.first_name, ' ', e.last_name) 'Employee Name',
    e.salary
FROM
    employees e
        INNER JOIN
    departments d ON d.department_name = 'IT'
WHERE
    e.salary > 70000;
-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : Create a summary that shows each department and the projects associated with its employees.
-- The output should include department name and project names.

SELECT 
    d.department_name,
    GROUP_CONCAT(p.project_name SEPARATOR ', ') AS 'Project Names'
FROM
    departments d
        INNER JOIN
    employees e ON e.department_id = d.department_id
        INNER JOIN
    projects p ON p.employee_id = e.employee_id
GROUP BY d.department_name;
-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : Identify employees who are not currently assigned to any projects.
-- Return their first name, last name, and department name.

SELECT e.first_name, e.last_name, d.department_name FROM employees e
LEFT JOIN projects p ON p.employee_id = e.employee_id 
LEFT JOIN departments d ON d.department_id = e.department_id
WHERE p.project_name is NULL;
-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : List the first name, last name, salary, and project names for all employees.
-- If an employee does not have a project, still include their salary but indicate the project name as NULL.
SELECT e.first_name, e.last_name, e.salary, GROUP_CONCAT(p.project_name SEPARATOR ', ') Projects FROM employees e
LEFT JOIN projects p ON p.employee_id = e.employee_id
GROUP BY e.first_name,e.last_name,e.salary;
-- ---------------------------------------------------------------------------------------------------------------------------------- --
-- Que : give names of employee and department whose project have started before '2023-03-05'  
SELECT 
    e.first_name, d.department_name
FROM
    employees e
        INNER JOIN
    projects p ON e.employee_id = p.employee_id
        INNER JOIN
    departments d ON d.department_id = e.department_id
WHERE
    p.start_date = '2023-03-05';
    
    
SELECT * from employees;
SELECT * FROM employees e WHERE e.salary < (SELECT MAX(salary) FROM employees) ORDER BY salary DESC LIMIT 1;
SELECT * FROM employees GROUP BY salary DESC;
SELECT * from employees ORDER BY salary DESC LIMIT 10 OFFSET 3; 