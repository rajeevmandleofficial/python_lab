# WAP to print only the even numbers present in a List of integers.

lst = [1, 2, 3, 4, 5, 6, 7, 8]

for i in lst:
    if i % 2 == 0:  # checking if i is even or not
        print(i, " ", end='')
