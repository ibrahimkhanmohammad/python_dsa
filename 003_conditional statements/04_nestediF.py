age = int(input("Enter your age: "))
has_cert = True

if age>=18:
    print("Hey! your age requirement met successfully")
    if has_cert:
        print("Congratulations! You can apply for this role as all your requirements validates")
    else:
        print("Sorry about that, as  you do not have any cert, you are unable to apply for this role")
else:
    print("Sorry! you are unable to apply for this role as your age is not validate")