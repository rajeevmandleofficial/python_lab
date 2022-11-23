n = input("Enter Number to calculate sum & average")
 
n = int (n)
 
sum = 0
 
for num in range(0, n+1, 1):
    sum = sum+num
     
average = sum / n
 
print("SUM of", n, "numbers is: ", sum )
print("Average of", n, "natural number is: ", average)
