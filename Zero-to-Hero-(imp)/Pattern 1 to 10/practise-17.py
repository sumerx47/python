accounts = {
    "ACC1001": {
        "name": "Ahmed",
        "balance": 25000,
        "pin": 1234
    },
    "ACC1002": {
        "name": "Sara",
        "balance": 8500,
        "pin": 5678
    },
    "ACC1003": {
        "name": "Zaid",
        "balance": 50000,
        "pin": 4321
    },
    "ACC1004": {
        "name": "Ayesha",
        "balance": 1200,
        "pin": 9876
    }
}


try:
    # Login
    account_number = input("Enter Account Number: ")

    if account_number not in accounts:
        raise ValueError("Account does not exist.")

    pin = int(input("Enter PIN: "))

    if accounts[account_number]["pin"] != pin:
        raise ValueError("Incorrect PIN.")

    print(f"\nWelcome {accounts[account_number]['name']}!")

    # Banking Menu
    while True:

        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print(f"Your balance is: ₹{accounts[account_number]['balance']}")

        # Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))

                if amount <= 0:
                    raise ValueError(
                        "Deposit amount must be greater than zero."
                    )

                accounts[account_number]["balance"] += amount

                print("Deposit successful!")
                print(f"Deposited: ₹{amount}")
                print(
                    f"New balance: ₹{accounts[account_number]['balance']}"
                )

            except ValueError as e:
                print(f"Error: {e}")

            

        # Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    raise ValueError(
                        "Withdrawal amount must be greater than zero."
                    )

                balance = accounts[account_number]["balance"]

                if amount > balance:
                    raise ValueError("Insufficient funds.")

                accounts[account_number]["balance"] -= amount

                print("Withdrawal successful!")
                print(f"Withdrawn: ₹{amount}")

            except ValueError as e:
                print(f"Error: {e}")

            finally: 
                print(f"Account balance: ₹{accounts[account_number]['balance']}")

        # Exit
        elif choice == "4":
            print("Thank you for using our banking system!")
            break

        # Invalid choice
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


except ValueError as e:
    print(f"Error: {e}")