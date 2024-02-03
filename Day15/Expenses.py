def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove? (Enter the expense number or 'q' to cancel)")
        try:
            choice = input("> ")
            if choice.lower() == 'q':
                break
            expenseToRemove = int(choice)
            if 0 <= expenseToRemove < len(expenses):
                del expenses[expenseToRemove]
                print("Expense removed successfully.")
                break
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index or 'q' to cancel.")

def addExpense():
    print("How much was this expense?")
    while True:
        try:
            amountToAdd = float(input("> "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("What category was this expense?")
    category = input("> ")

    expense = {'amount': amountToAdd, 'category': category}
    expenses.append(expense)
    print("Expense added successfully.")

def printMenu():
    print("\nPlease choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")
    print("4. Quit")

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    for i, expense in enumerate(expenses):
        print(f"# {i} - {expense['amount']} - {expense['category']}")
    print("\n\n")

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            addExpense()
        elif optionSelected == "2":
            removeExpense()
        elif optionSelected == "3":
            listExpenses()
        elif optionSelected == "4":
            print("Exiting the expense tracker. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")
