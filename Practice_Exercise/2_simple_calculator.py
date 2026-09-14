#defining functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
#Taking inputs from user
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
#Performing operations
print("Addition:",add(n1,n2))
print("Subtraction:",sub(n1,n2))
print("Multiplication:",mul(n1,n2))
print("Division:",div(n1,n2))

