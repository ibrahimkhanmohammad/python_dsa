'''
Write a function called square_num that takes a number and returns its square.
Store the result and print it.
'''

def square_num(num):
    return num ** 2

num = int(input('num: '))

print(f'Square of {num} is: ',square_num(num))