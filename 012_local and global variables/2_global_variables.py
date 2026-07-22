num1 = 10
num2 = 20

def addition(num1, num2):
    total = num1 + num2
    print(f'Total: {total}')
    print(num1, num2)
#     here it prints num1 as 1 and num2 as 2 because we passed arguments in the addition function.


addition(1, 2)
print(num1, num2)
#  here it prints num1 as 10 and num2 as 20 as it is global variable we can use it anywhere in the code, as it declared globally.