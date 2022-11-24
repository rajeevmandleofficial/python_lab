# WAP to demonstrate CRUD operations.
import mysql.connector as ctr

mydb = ctr.connect(
    host="localhost",
    user="root",
    password="",
    database="lab9")
mycursor = mydb.cursor()
# query = "CREATE TABLE student(name varchar(20),rollno int(20))"

# created database


n = int(input("Enter no of students "))

for i in range(n):
    name = input("enter your name :")
    rollno = int(input("enter your rollno :"))
    query = "insert into student values('{}','{}')".format(name, rollno)
    print(query)
    mycursor.execute(query)
mydb.commit()
