age=int(input("Enter Age:"))
if age>=18:
    id=input("Do you have an ID? (y/n):")
    if id=="y":
        print("You are Eligible to Vote")
    else:
        print("You are Not Eligible to Vote")
else:
    print("You are Not Eligible to Vote")