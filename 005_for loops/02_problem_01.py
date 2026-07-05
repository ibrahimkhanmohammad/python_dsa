# divisible by 2:

x = int(input("Enter x: "))

for i in range(1,x+1):
    if i%2==0:
        print(i, end=" ")

print("\n")
# divisible by both 2 and 3:  

x = int(input("Enter x: "))

for i in range(1,x+1):
    if i%2==0 and i%3==0:
        print(i, end=" ")
