class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        print(f"Welcome, {self.owner}! Your bank account has been created.")

    def perform_transaction(self, transaction_type, amount):
        print(f"\nTransaction: {transaction_type}")
        print(f"Amount: {amount}")
        print(f"Current Balance: {self.balance}")

        if transaction_type == "deposit":
            if amount > 0:
                self.balance += amount
                print(f"Deposit successful. New Balance: {self.balance}")
            else:
                print("Invalid deposit amount.")

        elif transaction_type == "withdraw":
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. New Balance: {self.balance}")
            elif amount > self.balance:
                print("Insufficient funds.")
            else:
                print("Invalid withdrawal amount.")

        elif transaction_type == "check_balance":
            print(f"Your balance is: {self.balance}")

        else:
            print("Invalid transaction type.")

        print("Thank you for using the bank.\n")


# Create an object of BankAccount
account1 = BankAccount("Abdullah", 5000)

# Perform multiple transactions
account1.perform_transaction("deposit", 1500)
account1.perform_transaction("withdraw", 2000)
account1.perform_transaction("withdraw", 6000)  # Should fail due to insufficient funds
account1.perform_transaction("check_balance", 0)
account1.perform_transaction("transfer", 1000)   # Invalid transaction
