# To get the data type of a variable, we can use the type() function:

# |-----------------------------------------------------------------------------------|
#                                      TYPE FUNCTION
# |-----------------------------------------------------------------------------------|

color = "Blue"
charecters = 4

print(type(color))  # <class 'str'>
print(type(charecters)) # <class 'int'>

# |-----------------------------------------------------------------------------------|
#                                   IS INSTANCE FUNCTION
# |-----------------------------------------------------------------------------------|

# The built-in isinstance() function lets you check if a variable matches a specific data type. It takes in an object and the type you want to check it against, then returns a boolean. Here are some examples:

print(isinstance('Hello world', str)) # True
print(isinstance(42, int)) # True
print(isinstance('John Doe', int)) # False
print(isinstance(True, bool)) # True
