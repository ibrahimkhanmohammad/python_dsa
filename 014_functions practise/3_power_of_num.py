'''
Write a function power(base, exp) that returns base raised to exp using a
loop - no ** operator or pow() allowed.
'''

def power(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

# Example
print(power(2, 5))   # 32
print(power(3, 4))   # 81
print(power(5, 0))   # 1