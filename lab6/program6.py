"""WAP to build a Dictionary to hold Name, Dept, Salary, DA and Gross of an employee. 
i.	Input the Name, Dept and Salary details from the user.
ii.	Calculate DA as 20% of the Salary
iii.	Gross = Salary + DA
iv.	Display all the contents"""


name = input("enter name of the employee :")
Dept = input("enter the departement :")
salary = float(input("enter your Salary :"))
da = (20 * salary)/100
gross = salary+da
dic1 = {"Name": name, "Dept": Dept, "Salary": salary, "DA": da, "Gross": gross}
print(dic1)
