# WAP to print the sum and average of all the elements in a List of numbers.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
summ = 0
lenth = len(lst)
for i in lst:
    summ += i
print("sum of all the elements in a list is {}".format(summ))
print("average of all the elements in a list is {}".format(summ/(lenth)))
