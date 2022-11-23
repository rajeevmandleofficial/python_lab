# WAP to read five subject names and their corresponding marks and store it in a dictionary. Display subject name with marks that is maximum and minimum.
l1 = {}
for i in range(5):
    a = input("Enter Subject Name :")
    b = float(input("Enter marks obtained :"))
    c = b
    l1[a] = b
values = list(l1.values())
max = values[0]
min = values[0]
for i in values:

    if i > max:
        max = i
    if i < min:
        min = i
for i in l1:
    if l1[i] == max:
        print("max marks : {} {}".format(i, l1[i]))
for i in l1:
    if l1[i] == min:
        print("min marks : {} {}".format(i, l1[i]))
