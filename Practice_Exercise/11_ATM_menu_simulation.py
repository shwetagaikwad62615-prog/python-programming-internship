balance =5000
#Taking choice from users
while True: 
    print("=====ATM Menu=====")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice =int(input("Enter your choice(1-4): "))
    #performing operations
    if choice ==1:
        print("Current Balance: ",balance)
    elif choice==2:
        d=int(input("Enter the Amount to Deposit: "))
        if d>0:
            balance +=d
            print("Deposit Successful...")
            print("Current Balance: ",balance)
        else:
            print("Invalid Amount")
    elif choice==3:
        w=int(input("Enter the Amount to Withdraw: "))
        if w>0 and w<=balance:
            balance -=w
            print("Withdrawal Successful...")
            print("Current Balance: ",balance)
        elif w>balance:
            print("Insufficient Balance." )
        else:
            print("Invalid Input.")

    elif choice==4:
            print("Thank You For Using the ATM.")
            break
    else:
        print("Invalid choice...")