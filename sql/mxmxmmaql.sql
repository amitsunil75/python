create database if not exists assignment_database;
use assignment_database;
create table if not exists countries(
country_id int not null primary key auto_increment,
country_name varchar(29) not null,
region_id int 
);
select * from countries;
alter table countries rename column country_id to country_refrence_id;

create database if not exists employee_dbms;
use employee_dbms;
drop table employee_database;
create table if not exists employee_database(
dept_id int primary key not null ,
dept_name varchar(50) not null,
mang_id int not null,
loc_id  int not null
);

-- insert into employee_database(
-- dept_id,
-- dept_name,
-- mang_id,
-- loc_id 
-- ) values
-- (10,'admin',200,1700),
-- (20,'mark',201,1800),
-- (30,'purch',114,1700),
-- (40,'hr',203,2400),
-- (50,'ship',121,1500),
-- (60,'it',103,1400),
-- (70,'pr',204,2700),
-- (80,'sal',145,2500),
-- (90,'exec',100,1700),
-- (100,'fininace',205,1700);
select dept_name,dept_id from employee_database;
select dept_name from employee_database where dept_id between 30 and 70;
select * from employee_database  where loc_id=1700;
create table new_emp(
emp_id int not null primary key auto_increment,
first_name varchar(50) not null,
last_name varchar(50) not null,
salary int not null,
join_date datetime not null,
dept_name  varchar(60) not null
);
-- insert into new_emp(first_name,last_name,salary,join_date,dept_name) values
-- ('bob','kinto',1000000,'2019-01-20','finance'),
-- ('jerry','kanto',6000000,'2019-01-15','it'),
-- ('philip','jsoeo',8900000,'2019-02-05','bank'),
-- ('john','abrao',2000000,'2019-02-25','insurnc'),
-- ('Michel','mathewo',2200000,'2019-02-28','finance'),
-- ('Alex','chrekko',4000000,'2019-05-10','it'),
-- ('Yohan','soso',12300000,'2019-06-20','bank');
select * from new_emp;
select * from new_emp order by first_name;
select * from new_emp where first_name='bob' or first_name='alex';
select * from new_emp where last_name like '%o';
select * from new_emp where first_name like '%n';
select * from new_emp where first_name like 'a%';
select * from new_emp;


