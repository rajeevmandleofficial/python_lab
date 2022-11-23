# WAP to create a List of numbers from 1 to 100, where each element should be completely divisible by 10. (hint: use comprehension)

newlist = [i for i in range(1, 101) if i % 10 == 0]
print(newlist)
