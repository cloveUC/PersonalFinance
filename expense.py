#Class made to set up the format for each expense to be added/shown
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"{self.description}: ${self.amount:.2f}"