# WAP to generate a user defined exception whenever a numeric value is found in a string which is input from the user.
x = eval(input("enter a string \n (do-not-enter-a-numberic-value :"))
class CustomError(Exception):
    pass
if type(x) == int:
    raise CustomError("Example of Custom Exceptions in Python")
