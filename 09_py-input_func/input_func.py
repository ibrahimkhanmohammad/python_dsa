#by default input returns str even if we pass any datatype like int, float
name = input("What is your name? ")
print(f"Hello, {name}")
print(type(name))

#use int when dealing with integers
age = int(input("What is your age? "))
print(f"You are {age} years old")
print(type(age))

#use float when dealing with decimals
salary = float(input("What is your salary? "))
print(f"He earns {salary} dollars")
print(type(salary))