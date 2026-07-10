class Account:
    def __init__(self, balance):
        self.totalamount = balance

    def deposit(self, amount):
        self.totalamount += amount

    def withdraw(self, amount):
        if amount > self.totalamount:
            print("Insufficient balance!")
        else:
            self.totalamount -= amount

    def show_balance(self):
        print("Current Balance:", self.totalamount)


# Ask for initial balance
balance = int(input("Enter initial balance: "))
acct = Account(balance)

while True:
    print("\nChoose an operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter amount to deposit: "))
        acct.deposit(amount)
        acct.show_balance()

    elif choice == "2":
        amount = int(input("Enter amount to withdraw: "))
        acct.withdraw(amount)
        acct.show_balance()

    elif choice == "3":
        acct.show_balance()

    elif choice == "4":
        print("Thank you for using the account.")
        break

    else:
        print("Invalid choice. Please try again.")
