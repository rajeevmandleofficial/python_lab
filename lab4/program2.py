# WAP to demonstrate how to traverse a list 1) using print(), 2) using while loop and 3) using for loop.

lst = [10, 20, 30, 40, 50, 60]
# ---------------------------------------------------------------------------
# using print()
# not using loop
# * symbol is use to print the list elements in a single line with space.
print(*lst)
# ---------------------------------------------------------------------------


# ----------------------------------------
# using while loop
n = len(lst)
i = 0
while (i < n):
    print(lst[i], end=' ')
    i += 1
print()
# -----------------------------------------


# ------------------------------------------
# using for loop

for i in lst:
    print(i, end=' ')
print()
# -------------------------------------------
