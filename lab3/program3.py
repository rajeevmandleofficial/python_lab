# Accept a five digit number and reverse the number. Show whether the reversed number is same as the original number or not.
x_original = int(input("Enter five digit number :"))
x = x_original
summ = 0
c = 10000

while x != 0:
    z = x % 10
    summ = summ + (z*c)
    c = c/10
    x = x//10
if (int(summ) == x_original):
    print("number is same when reversed")
else:
    print("number is not same when reversed")
