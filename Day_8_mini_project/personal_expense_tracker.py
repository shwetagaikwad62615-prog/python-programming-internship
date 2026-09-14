import csv
from datetime import datetime

#store all records
expenses = []

#validate and get expense amount 
def get_amount():
    while True:
        try:
            amount = float(input("Enter Expense Amount: "))

            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Please enter a valid amount.")

#Display categories 
def get_category():
    print("\n----- Categories -----")
    print("1. Food")
    print("2. Travel")
    print("3. Shopping")
    print("4. Bills")

    while True:
        choice = input("Enter Category (1-4): ")

        if choice == "1":
            return "Food"
        elif choice == "2":
            return "Travel"
        elif choice == "3":
            return "Shopping"
        elif choice == "4":
            return "Bills"
        else:
            print("Invalid category. Please choose 1-4.")

#Add new Expenses
def add_expense():
    name = input("Enter Expense Name: ")

    while name.strip() == "":
        print("Expense name cannot be empty.")
        name = input("Enter Expense Name: ")

    amount = get_amount()
    category = get_category()

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")            #takiing date &time from library

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date_time": date_time
    }

    expenses.append(expense)

    print("\nExpense Added Successfully.")

#Viewing Expenses
def view_expenses():
    if not expenses:                                #If their is no Expense
        print("\nNo Expenses Recorded.")
        return

    print("\n===== All Expenses =====")             #If expense is present 
    print("Name\t\tAmount\t\tCategory\t\tDate & Time")
    for expense in expenses:
        print(expense["name"],"\t\t",expense["amount"],"\t\t",expense["category"],"\t\t",expense["date_time"])
        print("------------------------")

#Calculate Total Expense
def calculate_total():
    if not expenses:                            #If their is no Expense
        print("\nNo Expenses Recorded.")
        return

    total = 0                                   #If their is expense

    for expense in expenses:                     #If their is expense
        total += expense["amount"]

    print("\nTotal Expenses:", total)

#Searching expense by category
def search_by_category():
    if not expenses:                            #If their is no Expense
        print("\nNo Expenses Recorded.")
        return

    category = get_category()                   #If their is expense
    found = False

    print("\n===== " + category + " Expenses =====")

    print("Name\t\tAmount\t\tCategory\t\tDate & Time")
    for expense in expenses:
        if expense["category"] == category:
            print(expense["name"], "\t\t", expense["amount"], "\t\t", expense["category"], "\t\t", expense["date_time"])
            print("------------------------")
            found = True

    if not found:                            #If Expense is not found
        print("No expenses found in this category.")

#To find Highest and Lowest Expense
def highest_lowest_expense():
    if not expenses:                           #If their is no Expense
        print("\nNo Expenses Recorded.")
        return

    highest = expenses[0]                      #If their is expense
    lowest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

        if expense["amount"] < lowest["amount"]:
            lowest = expense

    print("\n===== Highest Expense =====")
    print("Name:", highest["name"])
    print("Amount:", highest["amount"])
    print("Category:", highest["category"])
    print("Date & Time:", highest["date_time"])

    print("\n===== Lowest Expense =====")
    print("Name:", lowest["name"])
    print("Amount:", lowest["amount"])
    print("Category:", lowest["category"])
    print("Date & Time:", lowest["date_time"])

#To get Daily Summary of Expense
def daily_summary():
    if not expenses:
        print("\nNo Expenses Recorded.")
        return

    today = datetime.now().strftime("%Y-%m-%d")
    total = 0

    for expense in expenses:
        if expense["date_time"].startswith(today):
            total += expense["amount"]

    print("\n===== Daily Summary =====")
    print("Date:", today)
    print("Total Expenses:", total)

#To get monthly expense
def monthly_summary():
    if not expenses:
        print("\nNo Expenses Recorded.")
        return

    current_month = datetime.now().strftime("%Y-%m")
    total = 0

    for expense in expenses:
        if expense["date_time"].startswith(current_month):
            total += expense["amount"]

    print("\n===== Monthly Summary =====")
    print("Month:", current_month)
    print("Total Expenses:", total)

#to save file
def save_to_text_file():
    if not expenses:
        print("\nNo Expenses to Save.")
        return

    with open("expenses.txt", "w") as file:
        file.write("PERSONAL EXPENSE TRACKER\n")
        file.write("========================\n\n")
        print("Name\t\tAmount\t\tCategory\t\tDate & Time")
        for expense in expenses:
            print(expense["name"],"\t\t",expense["amount"],"\t\t",expense["category"],"\t\t",expense["date_time"])
            print("------------------------")

    print("\nExpenses saved to expenses.txt successfully...")

#export expense records to csv file
def export_to_csv():
    if not expenses:
        print("\nNo Expenses to Export...")
        return

    with open("expenses.csv", "w", newline="") as file:
        fieldnames = ["name", "amount", "category", "date_time"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)

    print("\nExpenses exported to expenses.csv successfully...")

#Taking user choice from menu   
while True:
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Search Expenses by Category")
    print("5. Highest and Lowest Expense")
    print("6. Daily Summary")
    print("7. Monthly Summary")
    print("8. Save Expenses to Text File")
    print("9. Export Expenses to CSV")
    print("10. Exit")

    choice = input("Enter Your Choice (1-10): ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        search_by_category()

    elif choice == "5":
        highest_lowest_expense()

    elif choice == "6":
        daily_summary()

    elif choice == "7":
        monthly_summary()

    elif choice == "8":
        save_to_text_file()

    elif choice == "9":
        export_to_csv()

    elif choice == "10":
        print("\nThank you for using Personal Expense Tracker...")
        break

    else:
        print("Invalid choice. Please select 1-10...")