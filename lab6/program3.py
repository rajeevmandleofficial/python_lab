# WAP to read five subject names and their corresponding marks and store it in a dictionary. Display that dictionary.
l1 = {}
for i in range(5):
    a = input("Enter Subject Name :")
    b = float(input("Enter marks obtained :"))
    l1[a] = b
print(l1)
