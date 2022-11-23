# WAP to convert the following string "the quick brown fox jumps over the lazy dog" into list of words and then create another list that contains uppercase words extracted from the previous list. Create another list that contains sub-list having uppercase words and its length. Use list comprehension.
strg = "the quick brown fox jumps over the lazy dog"

l1 = strg.split()
print(l1)
l2 = [i.upper() for i in l1]
print(l2)
l3 = [(i.upper(), len(i))for i in l1]
print(l3)
