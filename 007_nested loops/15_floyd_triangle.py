'''
1
2 3
4 5 6
'''

num = 1
for i in range(1, 4):
    for j in range(i):
        print(num, end=' ')
        num += 1
    print()