# WAP to demonstrate how to raise an inbuilt exception and a customized exception.
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise
