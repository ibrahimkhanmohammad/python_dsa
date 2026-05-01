# ==============================
# FOR LOOP ULTIMATE EXERCISE
# ==============================


# Q1: Print numbers divisible by 5 (1–50)
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

print("\n" + "="*30 + "\n")


# Q2: Print "even" for even numbers, else print number (1–20)
for i in range(1, 21):
    if i % 2 == 0:
        print("even")
    else:
        print(i)

print("\n" + "="*30 + "\n")


# Q3: Print squares from 1–10
for i in range(1, 11):
    print(i ** 2)

print("\n" + "="*30 + "\n")


# Q4: Print squares up to user input
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i ** 2)

print("\n" + "="*30 + "\n")


# Q5: Sum of numbers divisible by 7 (1–100)
total = 0
for i in range(1, 101):
    if i % 7 == 0:
        total += i
print("Sum:", total)

print("\n" + "="*30 + "\n")


# Q6: Count numbers divisible by both 3 and 5 (1–50)
count = 0
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        count += 1
print("Count:", count)

print("\n" + "="*30 + "\n")


# Q7: FizzBuzz (1–30)
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

print("\n" + "="*30 + "\n")


# Q8: Pattern - Increasing numbers
# 1
# 12
# 123
# 1234
# 12345
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "="*30 + "\n")


# Q9: Pattern - Decreasing numbers
# 5
# 54
# 543
# 5432
# 54321
for i in range(5, 0, -1):
    for j in range(5, i - 1, -1):
        print(j, end="")
    print()