from config.accounts import accounts

from services.banking import (
    login,
    deposit,
    withdraw
)

from exceptions.banking_exceptions import (
    AccountNotFoundError,
    InvalidPinError,
    InvalidAmountError,
    InsufficientFundsError,
    InvalidChoiceError
)


def main():

    try:

        account_number = input(
            "Enter Account Number: "
        ).strip()

        pin = int(
            input("Enter PIN: ")
        )

        account = login(
            accounts,
            account_number,
            pin
        )

        print(
            f"\nWelcome {account['name']}!"
        )

        while True:

            print("\n========== BANK MENU ==========")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            print("===============================")

            choice = input(
                "Enter your choice: "
            ).strip()

            if choice == "1":

                print(
                    f"\nBalance: "
                    f"₹{account['balance']:.2f}"
                )

            elif choice == "2":

                try:

                    amount = float(
                        input("Enter deposit amount: ")
                    )

                    deposit(
                        account,
                        amount
                    )

                except (
                    ValueError,
                    InvalidAmountError
                ) as e:

                    print(f"Error: {e}")

                else:

                    print(
                        "\nDeposit successful!"
                    )

                    print(
                        f"New balance: "
                        f"₹{account['balance']:.2f}"
                    )

                finally:

                    print(
                        "Transaction attempt completed."
                    )

            elif choice == "3":

                try:

                    amount = float(
                        input("Enter withdrawal amount: ")
                    )

                    withdraw(
                        account,
                        amount
                    )

                except (
                    ValueError,
                    InvalidAmountError,
                    InsufficientFundsError
                ) as e:

                    print(f"Error: {e}")

                else:

                    print(
                        "\nWithdrawal successful!"
                    )

                    print(
                        f"Remaining balance: "
                        f"₹{account['balance']:.2f}"
                    )

                finally:

                    print(
                        "Transaction attempt completed."
                    )

            elif choice == "4":

                print(
                    "\nThank you for using "
                    "our banking system!"
                )

                break

            else:

                raise InvalidChoiceError(
                    "Invalid choice."
                )

    except AccountNotFoundError as e:

        print(f"Login Error: {e}")

    except InvalidPinError as e:

        print(f"Login Error: {e}")

    except ValueError:

        print(
            "Login Error: PIN must be a number."
        )

    except InvalidChoiceError as e:

        print(f"Error: {e}")


if __name__ == "main":
    main()