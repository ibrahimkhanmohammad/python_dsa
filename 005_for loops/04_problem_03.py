# find the total_Sum of the nnumbers:

n = int(input("Enter n: "))
total_sum = 0

for i in range(1, n+1):
    total_sum+=i
 
print(total_sum, end=" ")