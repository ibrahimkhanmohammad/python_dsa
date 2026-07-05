# factors of a number:

num = int(input("enter the number: ")) 

for i in range(1,num+1):
    if num%i==0:
        print(i, end=" ")


print("\n")

# count no. of factors of a number:

num = int(input("enter the number: "))
count=0
for i in range(1,num+1):
    if num%i==0:
       count+=1
 
print(count)
    