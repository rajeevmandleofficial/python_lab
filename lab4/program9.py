# WAP to demonstrate the use of sort() of List class, to sort the elements of the List containing Strings based on string length. (Hint: use ‘key’ parameter)

x = input("Enter a string:")


print(sorted(x.split(), reverse=True))
