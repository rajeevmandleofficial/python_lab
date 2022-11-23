# WAP to create two Lists, the first List should contain only even numbers and second List should only contain odd numbers from a single main List of numbers.
list1 = [11, 22, 33, 44, 55]
listOdd = []
listEven = []


for num in list1:
    if num % 2 == 0:
        listEven.append(num)
    else:
        listOdd.append(num)

# print lists
print("list1:    ", list1)
print("listEven: ", listEven)
print("listOdd:  ", listOdd)
