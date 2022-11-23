# WAP to find whether an input number is prime or composite.
x = int(input("enter a number :"))
c = 0
for i in range(1, x+1):
    if (x % i == 0):
        c += 1
if c == 2:
    print("number is prime")
else:
    print("number is composite")
