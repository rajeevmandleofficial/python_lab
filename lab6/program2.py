# 2.	WAP to create two dictionaries, one should contain keys as even numbers and their respective values and another dictionary should contain as odd numbers and their respective values.List 1 contents are [1,2,3,4,5,6,7,8,9]. List 2 contents are extracted from the string "One Two Three Four Five Six Seven Eight Nine". Use Dictionary comprehension (Hint: use zip())
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s1 = "One Two Three Four Five Six Seven Eight Nine"
l2 = s1.split()
print(l1, l2)
deven = {k: v for k, v in zip(l1, l2) if k % 2 == 0}
print(deven)
dodd = {k: v for k, v in zip(l1, l2) if k % 2 != 0}
print(dodd)
