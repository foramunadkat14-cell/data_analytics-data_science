# SQL practice table

**order table**

1. create:

```
create table orders(
    order_id int AUTO_INCREMENT primary key,
    customer_id int,
    order_date date,
    total_amount decimal(10,2),
    payment_type varchar(100),
    shipping_address varchar(200),
    order_status varchar(100),
    delivery_date date
);
```

2. alter: 

```
alter table orders add discount decimal(10,2);
alter table orders drop payment_type;
alter table orders change shipping_address address varchar(200);
```

3. rename:

```
alter table orders rename to customer_orders;
```

4. drop:

```
drop table customer_orders;
```

5. truncate:

```
truncate table customer_orders;
```


**student table**

1. create:

```
create table student(
    student_id int AUTO_INCREMENT primary key,
    student_name varchar(100),
    course varchar(100),
    email varchar(100),
    mobile bigint,
    city varchar(100),
    admission_date date,
    fees decimal(10,2)
);
```


2. alter:

```
alter table student add age int after student_name;
alter table student drop city;
alter table student change student_name full_name varchar(100);
```

3. rename:

```
alter table student rename to college_student;
```

4. drop:

```
drop table college_student;
```

5. truncate:

```
truncate table college_student;
```

**library table**

1. create:

```
create table library(
    book_id int AUTO_INCREMENT primary key,
    book_name varchar(100),
    author_name varchar(100),
    category varchar(100),
    price decimal(10,2),
    publish_date date,
    stock int,
    language varchar(50)
);
```

2. alter:

```
alter table library add publisher varchar(100);
alter table library drop language;
alter table library change book_name title varchar(100);
```

3. rename:

```
alter table library rename to books_library;
```

4. drop:

```
drop table books_library;
```

5. truncate:

```
truncate table books_library;
```

**hotel table**

1. create:

```
create table hotel(
    hotel_id int AUTO_INCREMENT primary key,
    hotel_name varchar(100),
    owner_name varchar(100),
    city varchar(100),
    rating decimal(2,1),
    total_rooms int,
    contact_number bigint,
    opening_date date
);
```

2. alter:

```
alter table hotel add email varchar(100);
alter table hotel drop city;
alter table hotel change owner_name manager_name varchar(100);
```

3. rename:

```
alter table hotel rename to luxury_hotel;
```

4. drop:

```
drop table luxury_hotel;
```

5. truncate:

```
drop table luxury_hotel;
```


**hospital table**

1. create:

```
create table hospital(
    patient_id int AUTO_INCREMENT primary key,
    patient_name varchar(100),
    doctor_name varchar(100),
    disease varchar(100),
    admission_date date,
    discharge_date date,
    room_number int,
    bill_amount decimal(10,2)
);
```

2. alter:

```
alter table hospital add blood_group varchar(10);
alter table hospital drop room_number;
alter table hospital change patient_name name varchar(100);
```

3. rename:

```
alter table hospital rename to city_hospital;
```

4. drop:

```
drop table city_hospital;
```

5. truncate:

```
truncate table city_hospital;
```


**event table**

1. create:

```
create table event(
    event_id int AUTO_INCREMENT primary key,
    event_name varchar(100),
    organizer_name varchar(100),
    event_date date,
    venue varchar(100),
    ticket_price decimal(10,2),
    total_guests int,
    event_status varchar(50)
);
```

2. alter:

```
alter table event add sponsor_name varchar(100);
alter table event drop total_guests;
alter table event change organizer_name manager_name varchar(100);
```

3. rename:

```
alter table event rename to public_event;
```

4. drop:

```
drop table public_event;
```

5. truncate:

```
truncate table public_event;
```