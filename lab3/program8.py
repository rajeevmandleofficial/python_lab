# WAP to assume that uname=”ABC” and pswd=”123”. Ask user to enter the correct combination of uname and pswd. Print “Welcome to Python” only when both the uname and pswd are correct, otherwise keep on asking user to enter correct uname and pswd.
uname = "ABC"
pswd = "123"

while True:
    uname_ = input("enter username :")
    pswd_ = input("enter password :")
    if (uname_ == uname and pswd_ == pswd):
        print("Welcome to python")
        break
    else:
        print(" \n enter corrent password or username  ")
