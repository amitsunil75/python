create database if not exists student_database;
use student_database;
create table if not exists students(
 student_id int not null primary key auto_increment,
 student_name varchar(20) not null,
 student_age int(2),
 student_place varchar(20) not null
);
-- select * from students;
-- insert into students(student_name,student_age,student_place) values ('amit sunil',25,'kannur'),('aryan',23,'kozhikode'),('suhaib',30,'kozhikode');
-- select * from students;
-- alter table students add mark int not null;
select * from students;
update students set student_name='john',student_age=20 where student_id=2;
delete from students where student_id=5;
update students set mark=20 where student_id is not null limit 1000;
select distinct student_id,student_name,student_age from students;
