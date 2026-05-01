# Loop from 0 to 9 (default start = 0, end is excluded)
for num in range(10):
    print(num)


# Print a blank line for separation
print()
# Loop from 1 to 10 (end = 11 because range excludes last number)
for num2 in range(1, 11):
    print(num2)


print()
# Loop from 1 to 10 with step = 3
# So it jumps: 1 → 4 → 7 → 10
for num3 in range(1, 11, 3):
    print(num3)


print()
# Loop backwards from 10 to 1
# -1 means decreasing
for num4 in range(10, 0, -1):
    print(num4)


print()
# Loop through each character in a string
for character in "Hello!":
    print(character)