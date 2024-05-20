create database if not exists mydb;
use mydb;
create table if not exists country(
country_id int  primary key ,country_name varchar(20),
region_id int not null
);
alter table country rename  to coutry_del;
select * from coutry_del;
alter table coutry_del modify country_name varchar(20);
drop table coutry_del;

create table if not exists students(
id int not null primary key auto_increment,
names varchar(20),
class varchar(49),
mark int ,
gender enum('M','F')

);
insert into  students(names,class,mark,gender) values('as','five',85,'M');
alter table students rename column names to f_name;
select * from students;
delete from students where id=2;
select * from  students where id=7;
create table if not exists emploee_data(
id int not null primary key auto_increment,
dept_id int,
name varchar(29),
city varchar(50),
salary int
);

-- insert into emploee_data(dept_id,name,city,salary)
-- values
-- (1014,'ajay','banglore',580000),
-- (1014,'harry','delhi',290001),
-- (1003,'Anjali','banglore',340000),
-- (1023,'rahul','delhi',540000),
-- (1003,'anisha','chennai',670000);

-- select * from -- 
select * from emploee_data order by name desc;
select max(salary), min(salary), avg(salary) from emploee_data;

