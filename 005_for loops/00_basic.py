# basic program:

# here 1 is inclusive and 6 is excluisve so it runs from 1 to 5 only and instead of counter like used in while loops i+=1 here pyhton handles itself so use 1 but by default step is 1
for i in range(1,6,1):
    print(i, end = " ")

print("\n")


# here we used step = 2 to print from 1 to 10 excluding 11 such that the counter is +2 everytime like;
# 1 3 5 7 9

for i in range(1,11,2): 
    print(i, end =" ")