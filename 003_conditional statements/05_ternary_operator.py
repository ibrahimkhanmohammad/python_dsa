age = int(input("Enter your age: "))

# normal if-else:
'''
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
'''

# ternary operator:
# print("Eligible to vote") if age>=18 else print("Not eligible to vote")

# more pythonic way to use ternary operator:
status = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(status)