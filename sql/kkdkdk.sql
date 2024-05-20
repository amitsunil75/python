use mydb;
CREATE TABLE IF NOT EXISTS customer_data (
    id INT  NOT NULL ,
    customer_id INT NOT NULL,
    customer_name VARCHAR(20),
    created_at DATETIME,
    CONSTRAINT pk_customer_id PRIMARY KEY (customer_id) -- Define customer_id as primary key
);
 drop table customer_data;
create table if not exists orders(
order_id int primary key not null,
order_name varchar(20) not null,
order_date datetime not null,
customer_id INT NOT NULL,
constraint fk_customer_id foreign key (customer_id) references customer_data(customer_id)
);

-- insert into customer_data(id,customer_id,customer_name,created_at) values
-- (4,126,'shifana','2019-08-20');
select * from customer_data;
-- insert into orders(order_id,order_name,order_date,customer_id) values
-- (7,' beff friedrice','2024-06-28',128);
SELECT orders.order_name 
FROM orders
JOIN customer_data ON orders.customer_id = customer_data.customer_id
WHERE customer_data.customer_name = 'amit';
create table if not exists student(
id int not null primary key auto_increment,
name varchar(29) not null,
age int not null,
cid int not null
);
-- insert into  student(name,age,cid) values
-- ('dina',22,3),
-- ('sneha',25,2),
-- ('shahid',20,3),
-- ('anjana',21,1),
-- ('arsha',26,1),
-- ('nihal',23,2),
-- ('amal',25,4);

create table if not exists course(
id int not null primary key auto_increment,
cname varchar(29) not null,
fees int not null,
duration int not null
);
-- insert into  course(cname,fees,duration) values
-- ('data sc',60000,3),
-- ('data an',5000,2),
-- ('ba',45000,4),
-- ('st',35000,3);
select* from course;
select * from student;
select name,cname from student  inner join course on student.cid = course.id;
select count(name) from student inner join  course  on  student.cid = course.id where course.cname='ba';
select sum(fees) from student s inner join course c on s.cid=c.id where  c.cname='data sc';
select cname,count(name) as stdno from student s  inner join course c on  s.cid=c.id 
group by cname;
select name,cname,duration from student s inner join course c on s.cid=c.id order by name;

create  table if not exists employee_tb(
 id int not null primary key auto_increment,
 ename varchar(20) ,
 did int ,
 salary int,
 place varchar(20),
 pno int
);
create  table if not exists dept_tb(
 id int not null primary key auto_increment,
 dname varchar(20) ,
 location varchar(20)
);
create  table if not exists project_tb(
 id int not null primary key auto_increment,
 pname varchar(20) 
);
-- insert into employee_tb(ename,did,salary,place,pno)
-- values('sarun',1,50000,'KSD',2),('kavya',2,45000,'KNR',1),('anjana',2,40000,'CLT',1),('shilpa',1,35000,'PKD',2),
-- ('Fidha',3,25000,'CLT',3),('shehin',3,40000,'MPM',3),('shifana',2,30000,'KNR',1);

-- insert into dept_tb(dname,location)
-- values('FSD','Bengluru'),('DS','Hyderabad'),('DA','Mysore'),('ST','');

-- insert into project_tb(pname) values('Automation'),('Hotel Booking'),('Chat Analysis');
select * from employee_tb;
select * from dept_tb;
select * from project_tb;
select ename,dname from employee_tb et inner join dept_tb dt  on et.did=dt.id order by ename;
select count(ename) as employee_count,pname from employee_tb et inner join project_tb pt ON et.pno=pt.id group by pname;
select avg(salary) as average_salary,dname from employee_tb et inner join  dept_tb dt  on et.did=dt.id group by dname;
select dname from (
select avg(salary) as avgs,dname from employee_tb et inner join  dept_tb dt  on et.did=dt.id group by dname) as avarage_salary_dept
order by avgs  desc limit 1;

select count(*)as employee_count,pname  from employee_tb  et inner join project_tb pt ON et.pno=pt.id where pname='Chat Analysis';

