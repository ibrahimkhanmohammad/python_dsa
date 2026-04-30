username = "Jimmy"
#to access the string charecters we use string slicing usually every string starts with index 0 which each charecter is in it's own index, so the indexing is of 2 types: positive (0, 1, ...) and negative indexing (-1, -2, -3, ...)

#usually +ve indexing strats from left to right whereas the -ve indexing starts from right to left
# Accesses the character at index 0 ('J')
print(username[0])

# Slices from the start up to (but not including) index 4 -> "Jimm"
print(username[:4])

# Slices from index 4 to the very end -> "y"
print(username[4:])

# Slices from start to end (creates a full copy) -> "Jimmy"
print(username[:])

# Slices from the 4th character from the end to the finish -> "immy"
print(username[-4:])

# Slices the whole string but skips every other character (step of 2) -> "Jmy"
print(username[::2])

# Slices from index 0 to 4, taking every 3rd character (index 0 and 3) -> "Jm"
print(username[:4:3])

# Slices the whole string with a negative step, reversing it -> "ymmiJ"
print(username[::-1])