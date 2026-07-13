# break using For loop:

for i in range(1,11):
    if i == 6:
        break
    print(i, end=' ')


print('\n')


# break using while loop:

n = 1
while n <= 10:
    if n == 6:
        break
    print(n, end=' ')
    n += 1

print('\n')


# continue using For loop:

for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=' ')


print('\n')


# continue using while loop:

n = 1
while n <= 10:
    if n == 6:
        n+=1
        continue
    print(n, end=' ')
    n+=1