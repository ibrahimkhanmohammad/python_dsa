# print even numbers by taking input From the user both start, end and print From start to end by using while loop:

start = int(input("Enter num 1: "))
end = int(input("Enter num 2: "))

i = start

while i <= end:
    if i%2==0:
        print(i, end=" ")
    i+=1

