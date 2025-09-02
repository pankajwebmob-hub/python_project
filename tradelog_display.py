# Import the 'tabulate' function to display data in table format
from tabulate import tabulate
class Tradelog:
    # Constructor method to initialize the object with trade details
    def __init__(self, Tradetype, Status, Borrower, Lender, Currency, Amount, Rate, Term):
        self.Tradetype = Tradetype  # Assign the trade type to the object
        self.Status = Status
        self.Borrower = Borrower
        self.Lender = Lender
        self.Currency = Currency
        self.Amount = Amount
        self.Rate = Rate
        self.Term = Term

    # Method to return the trade details as a list (row) for tabulation
    def get_row(self):
        return [self.Tradetype, self.Status, self.Borrower, self.Lender,
                self.Currency, self.Amount, self.Rate, self.Term]


# Collecting input from user for each trade detail and storing in variables
Tradetype1 = input("Enter the Trade Type: ")
Status1 = input("Enter the Trade Status: ")
Brwr = input("Enter the Borrower Name: ")
Lndr = input("Enter the Lender Name: ")
Currency1 = input("Enter the Currency: ")
Amt = float(input("Enter the Amount: "))
Rate1 = float(input("Enter the Rate: "))
Term1 = input("Enter the Term: ")

# Create an instance (object) of Tradelog using the input data
Trade1 = Tradelog(Tradetype1, Status1, Brwr, Lndr, Currency1, Amt, Rate1, Term1)

# Define headers for the table display
headers = ["Trade Type", "Status", "Borrower", "Lender", "Currency", "Amount", "Rate", "Term"]
print("\nTrade Summary:\n")
# Print the trade details as a formatted table with headers using 'grid' style
print(tabulate([Trade1.get_row()], headers=headers, tablefmt="grid"))
