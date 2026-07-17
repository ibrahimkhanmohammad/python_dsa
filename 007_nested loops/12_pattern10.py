'''
3
3 2
3 2 1
3 2
3
'''

for i in range(3,0,-1):
    for j in range(3,i-1,-1):
        print(j, end=' ')
    print()
for i in range(2,4):
    for j in range(3,i-1,-1):
        print(j, end=' ')
    print()