# WAP to demonstrate the application of try, except, else and finally.
def fun(a):

    if a < 4:
        b = a/(a-3)
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")

else:
    print("no exception occured")
finally:
    print("This code is always executed!")
