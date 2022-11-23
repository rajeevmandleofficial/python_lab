# WAP to create a Login validator. Use Dictionary to hold all users and their passwords. The existing users should be able to login by entering correct username and password.

d1 = {"Rajeev": 123, "Rahul": 456, "Raj": 65}

while True:
    check = input("Do you want to login ? (yes/YES) :")
    if not (check == "yes" or check == "YES"):
        break
    name = input("Enter your login name:")
    pas = int(input("Enter your password :"))
    key = list(d1.keys())
    if name in key:
        if pas == d1[name]:
            print("logged in successfully !")
        else:
            print("incorrect password!")
    else:
        print("no user found !")
