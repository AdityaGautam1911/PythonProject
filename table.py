import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='123456',database='old')

mycursor=conn.cursor()

conn.autocommit = True

mycursor.execute("create table if not exists log_id(user_id varchar(20) ,password  varchar(100) primary key)")
print(">>>>log_id table successfully created!!!!")

mycursor.execute("create table if not exists office (em_no bigint,em_name varchar(255),em_dept varchar(255),em_salary int,em_age int)")
print(">>>>office table successfully created!!!!")

mycursor.execute("create table if not exists em_performance1 (em_no int,em_performance varchar(255),em_work varchar(255))")
print(">>>>performance table table successfully created!!!!")