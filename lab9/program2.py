# WAP to read student’s name, five subject names and their corresponding marks and
# store it in a database table for 5 students. Display that table contents.

import mysql.connector as ctr

mydb = ctr.connect(
    host="localhost",
    user="root",
    password="",
    database="lab9")
mycursor = mydb.cursor()
mycursor.execute("create table table2(name varchar(20), marks int(20) )")
for i in range(5):
    names = input("enter student's name :")
    marks = int(input(" enter your marks :"))
    query = "insert into table2 values('{}', '{}')".format(names, marks)
    mycursor.execute(query)
mydb.commit()
