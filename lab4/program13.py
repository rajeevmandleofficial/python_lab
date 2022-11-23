# WAP to create a list containing only the String length from each string present in another list of strings. Use list comprehension.
s = "my name is termux iam an terminal "

l1 = s.split()

l2 = [len(x) for x in l1]
print("list with lenth of string s for another list :", l2)
#
#
