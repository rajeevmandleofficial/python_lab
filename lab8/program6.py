# WAP to input name and age from user. The program should generate an exception if name or age are not in proper format i.e. age should be numeric and name should contain only alphabets.
class CustomError(Exception):
    pass


name = input("enter your name:")
age = int(input("enter you age:"))
if type(age) != int:
    raise CustomError(
        "age should be numeric and name should contain only alphabets.")
elif not (name.isalpha)():
    raise CustomError(
        "age should be numeric and name should contain only alphabets.")
