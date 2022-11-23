
# Python3 code to demonstrate working of
# Convert String to Tuple
# Using eval()
 
# initialize string
test_str = str(input("enter string : "))
 
# printing original string
print("The original string : " + str(test_str))
 
# Convert String to Tuple
# Using eval()
res = eval(test_str)
 
# printing result
print("Tuple after getting conversion from String : " + str(res))