#Class to manage each expense command
import csv
from expense import Expense
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

#Command to add expense
    def add_Expense(self, description, amount):
        expense = Expense(description, amount)
        self.expenses.append(expense)

#Command to view all expenses
    def view_Expense(self):
        #Updated to show index for deletion
        #for expense in self.expenses:
        #    print(expense)
        for index, expense in enumerate(self.expenses):
            print(f"{index + 1}. {expense}")

#Command to add all expenses and give the total
    def total_Expenses(self):
        return sum(expense.amount for expense in self.expenses)

#Command to save the expenses into a csv file, when given a name
    def save_expenses(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])
            for expense in self.expenses:
                writer.writerow([expense.description, expense.amount])

#Command to load csv file of expenses into the program, will fail if given invailid name
    def load_Expenses(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                next(reader) #skips the header
                self.expenses = [Expense(description, float(amount)) for description, amount in reader]
        except FileNotFoundError:
            print(f"The file {filename} does not exist.")

#Command to delete a previously added expense, uses the index shown when using the view_Expense() command 
    def delete_Expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense deleted successfully.")
        else:
            print("Invalid index. Please try again.")