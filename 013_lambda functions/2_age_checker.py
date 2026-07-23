# def is_adult(age):
#     if age >= 18:
#         return True
#     return False


#  we can use lambda function here because we can solve the problem with one line, i.e; through ternary operator.
#  Note : we cannot use for loop inside lamda function as it has several steps, as we cannot write inside lamda function within one line.

is_adult = lambda age: True if age >= 18 else False

print(is_adult(19))
print(is_adult(18))
