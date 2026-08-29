class AccountNotFoundError(Exception):
    pass


class InvalidPinError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class InvalidTransactionError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass


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


# =========================
# LOGIN
# =========================

try:
    account_number = input("Enter Account Number: ").strip()

    if account_number not in accounts:
        raise AccountNotFoundError(
            "Account does not exist."
        )

    try:
        pin = int(input("Enter PIN: "))

    except ValueError:
        print("Error: PIN must contain numbers only.")
        raise

    if accounts[account_number]["pin"] != pin:
        raise InvalidPinError("Incorrect PIN.")

    print(f"\nWelcome {accounts[account_number]['name']}!")

    # =========================
    # BANKING MENU
    # =========================

    while True:

        print("\n========== BANK MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        # =========================
        # CHECK BALANCE
        # =========================

        if choice == "1":

            print(
                f"\nYour current balance is: "
                f"₹{accounts[account_number]['balance']}"
            )

        # =========================
        # DEPOSIT
        # =========================

        elif choice == "2":

            try:
                amount = float(
                    input("Enter deposit amount: ")
                )

                if amount <= 0:
                    raise InvalidAmountError(
                        "Deposit amount must be greater than zero."
                    )

            except ValueError:
                print(
                    "Error: Deposit amount must be a valid number."
                )

            except InvalidAmountError as e:
                print(f"Error: {e}")

            else:
                accounts[account_number]["balance"] += amount

                print("\nDeposit successful!")
                print(f"Deposited: ₹{amount:.2f}")
                print(
                    f"New balance: "
                    f"₹{accounts[account_number]['balance']:.2f}"
                )

            finally:
                print("Transaction attempt completed.")

        # =========================
        # WITHDRAW
        # =========================

        elif choice == "3":

            try:
                amount = float(
                    input("Enter withdrawal amount: ")
                )

                if amount <= 0:
                    raise InvalidAmountError(
                        "Withdrawal amount must be greater than zero."
                    )

                balance = accounts[account_number]["balance"]

                if amount > balance:
                    raise InsufficientFundsError(
                        f"Insufficient funds. "
                        f"Available balance: ₹{balance:.2f}"
                    )

            except ValueError:
                print(
                    "Error: Withdrawal amount must be a valid number."
                )

            except InvalidAmountError as e:
                print(f"Error: {e}")

            except InsufficientFundsError as e:
                print(f"Error: {e}")

            else:
                accounts[account_number]["balance"] -= amount
                print("\nWithdrawal successful!")
                print(f"Withdrawn: ₹{amount:.2f}")
                print(
                    f"Remaining balance: "
                    f"₹{accounts[account_number]['balance']:.2f}"
                )
                
            finally:
                print("Transaction attempt completed.")
                print(
                    f"Account balance: "
                    f"₹{accounts[account_number]['balance']:.2f}"
                )

        # =========================
        # EXIT
        # =========================

        elif choice == "4":

            print(
                "\nThank you for using our banking system!"
            )
            break

        # =========================
        # INVALID CHOICE
        # =========================

        else:

            try:
                raise InvalidChoiceError(
                    "Invalid choice. Please select 1, 2, 3, or 4."
                )

            except InvalidChoiceError as e:
                print(f"Error: {e}")


# =========================
# LOGIN EXCEPTIONS
# =========================

except AccountNotFoundError as e:
    print(f"Login Error: {e}")

except InvalidPinError as e:
    print(f"Login Error: {e}")

except ValueError:
    print("Login Error: PIN must be a valid number.")

except Exception as e:
    print(f"Unexpected Error: {e}")
