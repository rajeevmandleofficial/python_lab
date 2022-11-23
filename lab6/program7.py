'''WAP to build a Dictionary to hold Name, Dept, AggMarks, AggPer and Div for a student.
v.	Input the Name and Dept details from the user.
vi.	Input marks of 5 subjects (out of 100) and store the aggregate in AggMarks.
vii.	percentage out of 500 and store in AggMarks.
viii.	Display all the contents'''
name = input("Enter name of the student :")
Dept = input("Enter department of the student:")
summ = 0
for i in range(5):
    a = float(input("Enter your marks :"))
    summ += a
aggmarks = summ/5
