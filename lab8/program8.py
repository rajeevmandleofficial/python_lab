# WAP to develop a Name verifier, if the name contains any special symbol or numeric value then the program should generate a customized exception to indicate that only alphabets are allowed. The verification should be done using a dedicated method (eg. verifyName(String nm))"""
class CustomError(Exception):
    pass


name = input("enter your name :")


def verifyName(name):
    if not (name.isalpha()):
        raise CustomError("only alphabets are allowed")


verifyName(name)
