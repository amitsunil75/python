create database if not exists student_dta;
use student_dta;
create table if not exists student_data(
id int not null auto_increment primary key,
name varchar(20) not null,
age int(2),
mark int not null
);
drop table student_data;
create table if not exists student_data(
id int not null auto_increment primary key,
name varchar(20) not null,
age int(2),
mark int not null
);

select * from student_data;
insert into student_data values(1,'amit',23,23);
insert into student_data values(2,'arayan',23,23);
select * from student_data;
alter table student_data add address varchar(40) after mark;
select * from student_data;
alter table student_data add active_status bool first;
SELECT * FROM student_data;
ALTER TABLE student_data MODIFY COLUMN active_status VARCHAR(20);
SELECT * FROM student_data;
ALTER TABLE student_data CHANGE COLUMN  active_status state VARCHAR(20);
select * from student_data;
alter table student_data drop column state, drop column address;
select * from student_data;
-- describe student_data
drop table student_data;
create table if not exists student_data(
id int not null primary key auto_increment,
name varchar(20) not null,
age int(2),
mark int not null
);
alter table student_data auto_increment=100;
insert into student_data(name,age,mark) values('amit',23,100),('amits',23,100);
select * from student_data;
