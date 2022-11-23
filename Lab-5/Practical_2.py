
# WAP to print the sum and average of all the elements in a Tuple of numbers.
gven_tupl = (12, 1, 45, 20, 10, 15, 35)

sum_tupl = 0

for elemt in gven_tupl:
  sum_tupl = sum_tupl + elemt

print("The Sum of the given tuple elements", gven_tupl, "=", sum_tupl)
print(sum(gven_tupl)/len(gven_tupl))