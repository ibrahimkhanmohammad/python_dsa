'''
    1
  1 2
1 2 3
'''

for i in range(1,4):
    for k in range(1,4-i):
        print(' ', end=' ')
    for j in range(1,i+1):
        print(j, end=' ')
    print()