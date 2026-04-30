age = int(input("Enter your age: "))

if age <= 0:
    print("Invalid age.")
elif 0 < age <= 13:
    print("You're child.")
elif 13 < age <= 19:
    print("You're teen.")
elif 19 < age <= 59:
    print("You're adult.")
else:
    print("You're senior.")