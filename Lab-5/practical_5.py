#WAP to create two Tuples, the first Tuple should contain only even numbers and 
# second Tuple should only contain odd numbers from a single main Tuple of numbers. Use tuple comprehension.
list1 = [10,6,7,45,89,90,1,225,76]
list2 = []
list3= []
for i in list1:
  if i % 2 == 0:
    list2.append(i)
print("Even numbers are : ",list2)   
for i in list1:
    if i%2 != 0:
        list3.append(i)
print("Odd numbers are : ",list3)
        