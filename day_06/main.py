# a welcome
print("\nWelcome To Budget Tracker\n")



balance = 0
transactions = {
                "income":[],
                "expense":[]
}
options = [1,2,3,4,5]
while True:
    
    # print options to select from
    print(f"\n{'-' * 20}")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. Exit")
    
# take an input
    try:

        # choose an option
        selected_option = int(input("Choose an option (1,2,3,4,5): "))
        if selected_option in options: 
            # Add Balance
            # if option is add expense
            if selected_option == 1:

                # income description input
                income_description = input("Enter income description (Salary, Bonus etc.): ")

                # handle amount description
                try:
                    income_amount = int(input("Enter amount: "))
                    if income_amount >= 1:
                        balance +=   income_amount
                        transactions['income'].append(f"{income_description} - {income_amount}")

                        print(f"\n{income_amount} Registered as income!")
                        print(income_amount, "Added to balance!")
                    else:
                        print("\nPlease record income in positive numbers.")

                except ValueError:
                    print("Please provide amount in numbers")


            # Add Expense
            elif selected_option == 2:
                expense_description = input("Enter expense description (Shopping, Coffee etc.): ")
                        

                try:
                    expense_amount = int(input("Enter expense amount: "))
                    if expense_amount >= 1:
                        balance -= expense_amount

                        transactions['expense'].append(f"{expense_description}: {expense_amount}")

                        print(f"\n{expense_amount} Registered as expense!")
                        print(expense_amount, "Reduced from balance!")

                    else:
                        print("\nPlease record expense in positive numbers.")

                except ValueError:
                    print("Please provide amount in numbers.")

            # show balance
            elif selected_option == 3:
                print("\nCurrent balance:", balance)   

            # show each transaction
            elif selected_option == 4:
                
                print("\nIncome Transactions")
                for i in transactions['income']:
                    print(f" - {i}")
                
                print("\nExpense Transactions")
                for e in transactions['expense']:
                    print(f"- {e}")
                    
            # Exit
            elif selected_option == 5:
                break
        else:
            print("\nInvalid input, only 5 options are available!")        
            print("Choose again!")        
            

    except ValueError:
        print("Invalid input")
        print("Please choose options between: 1,2,3,4 or 5")