sub_marks=int(input("Enter your marks: "))

if sub_marks>100 or sub_marks<0:
    print("Invalid")
elif sub_marks>=90:
    print("Grade A")
elif sub_marks>=80:
    print("Grade B")
elif sub_marks>=60:
    print("Grade C")
elif sub_marks>=45:
    print("Grade D")
else:
    print("Fail")

print("code executed successully.")