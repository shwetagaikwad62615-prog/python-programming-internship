marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade: A")
elif marks>=75 and marks<90:
    print("Grade: B")
elif marks>=50 and marks<75:
    print("Grade: C")
else:
    print("Grade: Fail")
