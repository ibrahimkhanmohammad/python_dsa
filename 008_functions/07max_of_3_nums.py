def max_nums(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print(f'{num1} is max of the 3 numbers.')
    elif num2 > num1 and num2 > num3:
        print(f'{num2} is max of the 3 numbers.')
    else:
        print(f'{num3} is max of the 3 numbers.')

max_nums(10, 30, 30)