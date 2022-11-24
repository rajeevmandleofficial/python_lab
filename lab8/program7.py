# WAP to input age from user. The program should generate an exception if age contains any non-numeric data or if the age entered is below 1 or above 90.
class CustomError(Exception):
    pass


age = (input("enter you age:"))
age2 = int(age)
if age2 > 90 or age2 < 1 or not (age.isnumeric)():
    raise CustomError("this is an exception custom made")
