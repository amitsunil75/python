for x in range(1,5):
        print('*'*x)
# output:
# *
# **
# ***
# ****
for x in range(5,1,-1):
        print('*'*x)

# *
# **
# ***
# ****
# *****
# ****
# ***
# **


# Draw upper part of the butterfly (left wing)
for x in range(1, 5):
    print('*' * x + ' ' * (5 - x) + '*' * x)

# Draw lower part of the butterfly (right wing)
for x in range(4, 0, -1):
    print('*' * x + ' ' * (5 - x) + '*' * x)

# output:
# *    *
# **   **
# ***  ***
# **** ****
# **** ****
# ***  ***
# **   **
# *    *
# Draw the upper part of the puppy
for i in range(3):
    print(" " * (3 - i) + "*" * (i * 2 + 1) + " " * (12 - i * 4) + "*" * (i * 2 + 1))

# Draw the middle part of the puppy
for i in range(3):
    print(" " * 3 + "*" * 7 + " " * 5 + "*" * 7)

# Draw the lower part of the puppy
for i in range(3):
    print(" " * (i + 1) + "*" * (7 - i * 2) + " " * (10 + i * 4) + "*" * (7 - i * 2))

# output:
#   *            *
#   ***        ***
#  *****    *****
#    *******     *******
#    *******     *******
#    *******     *******
#  *******          *******
#   *****              *****
#    ***                  ***
print('\n')

# Draw the upper part of the cat
for i in range(2):
    print(" " * (4 - i * 2) + "*" * (i * 4 + 3))

# Draw the middle part of the cat
print(" " * 3 + "*" * 3 + " " * 4 + "*" * 3)

# Draw the lower part of the cat
for i in range(2):
    print(" " * (i * 2 + 1) + "*" * (5 - i * 2))

# output:
#   ***
#   *******
#    ***    ***
#  *****
#    ***

print('\n')


# Draw the horizontal line of the T-bar
for _ in range(5):
    print("*", end="")
print()

# Draw the vertical lines of the T-bar
for _ in range(3):
    print(" " * 2 + "*", end="")
    print()
# output:
# *****
#   *
#   *
#   *