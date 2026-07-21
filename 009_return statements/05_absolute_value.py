'''
Write a function called absolute_value that takes a number and returns
its absolute value without using the built-in abs() function.
'''

def absolute_value(num):
    if num < 0:
        return -num
    return num

print(absolute_value(-10))
print(absolute_value(10))
print(absolute_value(0))

# with built-in abs func:
'''
def absolute_value(num):
    return abs(num)

print(absolute_value(-10))
print(absolute_value(10))
'''