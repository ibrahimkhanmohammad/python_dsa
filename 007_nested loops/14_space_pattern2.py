'''
    3
  3 2
3 2 1
'''

for i in range(3, 0, -1):
    for k in range(1, i + 1 - 1):
        print(' ', end=' ')
    for j in range(3, i-1, -1):
        print(j, end=' ')
    print()