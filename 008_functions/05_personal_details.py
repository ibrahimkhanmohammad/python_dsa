def details(name, age, gender):
    print(f'Hello {name}! You\'re {age} years old and you\'re a {gender}.')

details('Ibrahim', 20, 'male')


# if we want to take input from user:
def details(name, age, gender):
    print(f'Hello {name}! You\'re {age} years old and you\'re a {gender}.')

name = input('What is your name? ')
age = int(input('How old are you? '))
gender = input('What is your gender? ')
details(name, age, gender)