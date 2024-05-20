create database if not exists new_db;
use new_db;
create table if not exists employees(
id int primary  key auto_increment,
name varchar(50),
age int,
sex enum('m','f'),
dept_name varchar(20),
hiring_date datetime,
salary int
);

-- insert into employees(id,name,age,sex,dept_name,hiring_date,salary) values
-- (1,'david',56,'m','marketing','2010-01-24',56000),
-- (2,'savid',39,'m','sales','2010-02-12',30000),
-- (3,'neena',36,'f','accounting','2015-01-07',266000);
select count(*) as employee_count from   employees;
select * from employees;
select name,salary as least_salary from   employees order by salary  limit 1;
select  name,age  from employees order by age;
create table if not exists employees2(
id int primary  key auto_increment,
fname varchar(50),
lname varchar(50),
gender enum('m','f'),
dept_name varchar(20),
salary int
);
-- insert into employees2(id,fname,lname,gender,dept_name,salary) values
-- (1,'vikas','kv','m','it',500000),
-- (2,'ashish','kv','m','it',550000),
-- (3,'nickhil','dv','m','it',700000),
-- (4,'nickhil','dv','m','it',700000),
-- (5,'jishnu','br','m','eee',150000),
-- (6,'hello','br','m','eee',150000);

select  fname from employees2;
select distinct dept_name from employees2;
DELIMITER //

CREATE FUNCTION get_employee_count()
RETURNS VARCHAR(100) DETERMINISTIC
BEGIN
    DECLARE emp_count INT;
    DECLARE message VARCHAR(100);
    
    SELECT COUNT(*) INTO emp_count FROM employees;
    
    IF emp_count = 0 THEN
        SET message = 'No employees found.';
    ELSE
        SET message = CONCAT('Total number of employees: ', emp_count);
    END IF;
    
    RETURN message;
END//

DELIMITER ;

select get_employee_count() as employee_count;
DELIMITER $$
create function checK_employee_name(mname varchar(50))
returns varchar(100) DETERMINISTIC
Begin 
select name from emp