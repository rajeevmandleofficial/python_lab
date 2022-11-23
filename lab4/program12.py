# 12.	WAP to create a list L1 of integers from 1 to 10. From L1 create another list L2 with the condition that at positions having even numbers in L1 that even number will be inserted in L2 else 0 will be inserted. Use list comprehension.

l1 = [x for x in range(1, 11)]
print("l1 = ", l1)
l2 = [x if x % 2 == 0 else 0 for x in l1]
print("l2 = ", l2)
