marks=float(input("Enter your Marks: "))
if marks>=90:
    grade ="A"
elif marks>=75 and marks<=90:
    grade ="B"
elif marks>=60 and marks<=75:
    grade ="C"
elif marks>=45 and marks<=60:
    grade ="D"
else:
    grade ="F"
print("Grade: ",grade)