# print From start to end, numbers only divisible by 3 & 4:

start = int(input("Enter num 1: "))
end = int(input("Enter num 2: "))

i = start

while i <= end:
    if i%3==0 and i%4==0:
        print(i, end=" ")
    i+=1
