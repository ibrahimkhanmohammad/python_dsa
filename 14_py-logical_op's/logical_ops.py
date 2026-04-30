#in logical operators there are 3:  and, or, not
# in which and must have to be True in every case, in or even one True will be okay, and in not it's reverse of its bool type

age = 18
print(age>=18 and age<=20)
print(age>18 and age<=20)
print(age<=18 or age>20)
print(not age>18 or age>20)