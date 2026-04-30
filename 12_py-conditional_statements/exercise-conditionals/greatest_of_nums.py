num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))

if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 == num_2:
    print(f"{num_1} is same as {num_2}")
else:
    print(f"{num_1} is less than {num_2}")