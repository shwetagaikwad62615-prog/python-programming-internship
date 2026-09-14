#Taking inputs
n1=float(input("Entre the  First number: "))
n2=float(input("Enter the Second number: "))
print("\n1.Addition")
print("\n2.Substraction")
print("\n3.Multiplicaton")
print("\n4.Division")
choice=int(input("Enter your choice(1-4): "))
#Performing operations and printing results
if choice == 1:
    print("Addition: ",n1+n2)
elif choice ==2:
    print("Substraction: ",n1-n2)
elif choice ==3:
    print("Multiplication: ",n1*n2)
elif choice==4:
    if n2 !=0:
        print("Divivsion: ",n1/n2)
    else:
        print("Cannot divide by 0.")
else:
    print("Invalid Choice.")



