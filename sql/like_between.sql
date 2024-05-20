create database if not exists employee_database;
use employee_database;
 create table if not exists employee(
 employeeId int not null primary key auto_increment,
 first_name varchar(20) not null,
  last_name varchar(20) not null,
 age int(2),
 gender varchar(10),
 salary int(20) not null
);

  -- insert into employee(first_name,last_name,age,gender,salary) values ('chris','sale','21','M',91500),('david','price','22','M',300000),('keli','pedroia','23','F',125000),('andrew','benin','23','M',5000),('diana','betts','31','F',5600),('PABLO','SAN','27','M',170000),('xander','bog','23','M',6500),('saneo','ram','28','F',220000),('rick','poec','22','M',26000),('erin','brad','29','F',36000),('susu','More','22','F',57000);
 -- select * from employee;
 create table if not exists employee2 as select * from employee  where age<25 and gender='F' ;
--  insert into employee2(first_name,last_name,age,gender,salary) values ('allan','poe','20','M',2000);
 --  select first_name,last_name,salary from employee2  where salary >100000;
  delete  from employee where employeeId and  gender='M';
    select * from employee;
  
create table if not exists employee3(
 emp_id int not null primary key auto_increment,
 emp_name varchar(20) not null,
 emp_age int(2),
 city varchar(10),
 income int(20) not null
) 
auto_increment=101;
-- insert into employee3(emp_name,emp_age,city,income) values ('peter','20','Nyk',200000),('Mark','32','cal',300000),('donal','40','ariz',100000),('obma','35','flori',5000),('linkon','38','georgia',250000),('Kane','45','Alaska',450000),('adam','52','cal',500000),('mac','28','flori',350000);
select * from employee3;
select * from employee3 where city like 'a%';
select * from employee3 where city like '%a';
select * from employee3 where city not like '%a';
select * from employee3 where emp_name like '%a';
select * from employee3 where emp_name like '%te%';
-- select * from employee3 where city like '%te%';
select * from employee3 where city like '__i%';
select * from employee3 where city like '%i_';
select * from employee3 where city like 'a_%z';
select * from employee3 where city like '_a%i';
select * from employee3 where emp_age in (20,32,33,27,40);
select * from employee3 where emp_age between 20 and 39;
select * from employee3 where emp_age is  null;

