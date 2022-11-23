# WAP to remove duplicate elements from a list and create a new list with those unique elements. (Hint: use in and not in )

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))
res = []
[res.append(x) for x in test_list if x not in res]

print("The list after removing duplicates : "
      + str(res))
