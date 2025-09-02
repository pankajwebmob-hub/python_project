
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Manufacturing Year: {self.year}")

# Create objects
car1 = Car("Tata", "Safari", 2025)
car2 = Car("Toyota", "Camry", 2020)

# Call method to display info
car1.display_info()
print("---")
car2.display_info()
print("---")


class Tradelog:
    def __init__(self,Tradetype, Status, Borrower, Lender, Currency, Amount, Rate, Term):
        self.Tradetype = Tradetype
        self.Status = Status
        self.Borrower = Borrower
        self.Lender = Lender
        self.Currency = Currency
        self.Amount = Amount
        self.Rate = Rate
        self.Term = Term

    def show_info(self):
        print(f"Trade Type: {self.Tradetype}")
        print(f"Trade Status: {self.Status}")
        print(f"Borrower Name: {self.Borrower}")
        print(f"Lender Name: {self.Lender}")
        print(f"Trade Currency: {self.Currency}")
        print(f"Trade Amount: {self.Amount}")
        print(f"Trade Rate: {self.Rate}")
        print((f"Trade Term: {self.Term}"))

Tradetype1 = input("Enter the Trade Type: ")
Status1 = input("Enter the Trade Status:")
Brwr = input("Enter the Borrower Name:")
Lndr = input("Enter the Lender Name: ")
Currency1 = input("Enter the Currency name:")
Amt = float(input("Enter the Amount: "))
Rate1 = float(input("Enter the Rate: "))
Term1 = input("Enter the Term:")

Trade1 = Tradelog(Tradetype1, Status1, Brwr, Lndr, Currency1, Amt, Rate1)
print("\nTrade Details:\n")
Trade1.show_info()

