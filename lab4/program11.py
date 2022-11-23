'''WAP to create a list whose elements are squares of integers from 1 to 10. 1) Implement without list comprehension and 2) Implement with list comprehension.'''
# without comprehension
x_list = []
for i in range(1, 11):
    x_list.append(i**2)

print("{} without using list comprehension".format(x_list))

# with comprehension
x = [x**2 for x in range(1, 11)]
print("{} with using list comprehension".format(x_list))
