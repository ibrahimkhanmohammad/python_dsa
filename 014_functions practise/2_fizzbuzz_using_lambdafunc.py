fizzbuzz = lambda num:(
    'fizzBuzz' if num % 3 == 0 and num % 5 == 0
    else 'fizz' if num % 3 == 0
    else 'buzz' if num % 5 == 0
    else num
)

print(fizzbuzz(15))
print(fizzbuzz(5))
print(fizzbuzz(8))