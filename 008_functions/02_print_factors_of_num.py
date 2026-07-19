def print_factors():
    num = int(input('num: '))
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')

print_factors()