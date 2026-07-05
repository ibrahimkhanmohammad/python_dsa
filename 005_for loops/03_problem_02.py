# ask start, end From the user and loop From start to end and From end to start:

start = int(input("Enter num 1: "))
end = int(input("Enter num 2: "))

for i in range(start, end+1):
    print(i, end=" ")

print("\n")
 
for i in range(end, start-1, -1):
    print(i, end=" ")
