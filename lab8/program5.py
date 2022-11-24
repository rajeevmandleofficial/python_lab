# WAP to generate a user defined exception whenever a special symbol is found in a string which is input from the user.
x = (input("enter a string :"))


class CustomError(Exception):
    pass


for i in x:
    if ord(i) in range(32, 47+1) or ord(i) in range(58, 64+1) or ord(i) in range(91, 96+1) or ord(i) in range(123, 126+1):
        raise CustomError("Example of Custom Exceptions in Python")
