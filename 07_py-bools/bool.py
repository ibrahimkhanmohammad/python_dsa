is_loggedin = True
has_access = False

print(has_access)
print(is_loggedin)

print(type(is_loggedin))
print(type(has_access))

#Non-zero numbers and content-filled strings are always True.
print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(-3.2))
print(bool(""))
print(bool(None ))
print(bool(" "))
print(bool("hello"))
print(bool([]))
print(bool([0]))
print(bool([3]))