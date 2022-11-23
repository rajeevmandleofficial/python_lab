# WAP to print the List elements using positive and negative indexing.

# using positive indexing
lst = [20, 39, 55, 34, 65, 23, 645, 2, 8, 56, 2]
n = len(lst)
for i in range(n):
    print(lst[i], end=' ')
print()
# using negative indexing
for i in range(-1, -(n+1), -1):
    print(lst[i], end=' ')
