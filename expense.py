#Class made to set up the format for each expense to be added/shown
class Expense:
    def __init__(self, description, category, date, amount):
        self.description = description
        self.category = category
        self.date = date
        self.amount = amount

    def __str__(self):
        return f"{self.description}, {self.category}, {self.date}: ${self.amount:.2f}"