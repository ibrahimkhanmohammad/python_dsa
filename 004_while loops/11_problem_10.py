# count the no. oF Factors

x = int(input("x: "))
counter = 0
i=1
while i<=x:
    if x%i==0:
        counter+=1
    i+=1
    
print(counter)