#Entering number as 0 will cause a runtime error
'''
number =int(input("Enter a number: "))
result =10/number
print("Result: ",result)
'''
#Corrected code:
number =int(input("Enter a Number: "))
if number !=0:
    result = 10/number
    print("Result: ",result)
else:
    print("Error: Division by zero is not allowed.")
