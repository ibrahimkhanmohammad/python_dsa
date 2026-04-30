age = int(input("Enter your age: "))

if age >= 18:
    print("Yes, you're eligible to vote.")
elif age <= 0:
    print("Invalid age factor.")
else:
    print("No, you're not eligible to vote.")