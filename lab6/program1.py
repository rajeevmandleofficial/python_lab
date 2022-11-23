# 1.	WAP to build a dictionary from two lists, one containing names of 5 usernames and another list containing their passwords. Use dictionary comprehension. (Hint: use zip())
l1 = ['rajeev', 'dhananjay', 'dhaman', 'sanjeev', 'rocky']
l2 = [12, 34, 56, 78, 90]
d1 = {k: v for k, v in (zip(l1, l2))}
print(d1)
