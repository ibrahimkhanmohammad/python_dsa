count = 0

def increase():
    global count # global keyword explicitly used for to add inside any function so that we can access to the original global variable declared outside any function.
    count += 2
    print(count)

increase()
print(count)