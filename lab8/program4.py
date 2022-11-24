# WAP to generate a user defined exception whenever a character value is found in a string which is input from the user.
x = (input("enter a string :"))


class CustomError(Exception):
    pass


for i in x:
    if ord(i) in range(0, 255+1):
        raise CustomError("Example of Custom Exceptions in Python")
