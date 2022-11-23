# WAP to determine whether the input number is an Armstrong number or not. (Hint: sum of cubes  = number itself)
x_original = int(input("Enter a number :"))
summ = 0
x = x_original
while x != 0:
    z = x % 10
    summ = summ + (z**3)
    x = x//10
if summ == x_original:
    print("{} is armstrong number ".format(x_original))
else:
    print("{} is not an armstrong number ".format(x_original))
