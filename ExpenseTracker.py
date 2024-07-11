#Main code to bring all classes together
from tracker import ExpenseTracker
from expense import Expense
from datetime import date

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu")
        print("1. Add a new expense")
        print("2. Delete an expense")
        print("3. View all expenses")
        print("4. Calculate total expenses")
        print("5. Save expenses to a file")
        print("6. Load expenses from file")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            #make addition
            description = input("Enter the expense description: ")
            print("1. Housing")
            print("2. Transportation")
            print("3. Food")
            print("4. Utilities")
            print("5. Medical")
            print("6. Savings")
            print("7. Personal Spending")
            print("8. Misc")

            category = int(input("Enter your category number: "))
            date = input("Hit enter for current date or enter date of expense(yyyy/mm/dd): ")
            if date == "":
                date = date.today()
            
            amount = float(input("Enter the expense amount: "))
            tracker.add_Expense(description, category, date, amount)
        elif choice == '2':
            #make deletion
            index = int(input("Enter the expense index to delete: "))
            tracker.delete_Expense(index)    
        elif choice == '3':
            #make to show all expenses
            tracker.view_Expense()
        elif choice == '4':
            #make to add all expenses and show total
            total = tracker.total_Expenses()
            print(f"Total expenses: ${total:.2f}")
        elif choice == '5':
            #make to save file when given a name
            filename = input("Enter the filename to save expenses: ")
            tracker.save_expenses(filename)
        elif choice == '6':
            #make to load a file when given a valid filename
            filename = input("Enter the filename to load expenses: ")
            tracker.load_Expenses(filename)
        elif choice == '7':
            #make to exit program
            break
        else:
            print("Invalid choice. Please choose 1-6")

if __name__ == "__main__":
    main()