from exceptions.banking_exceptions import (
    AccountNotFoundError,
    InvalidPinError,
    InvalidAmountError,
    InsufficientFundsError
)


def login(accounts, account_number, pin):

    if account_number not in accounts:
        raise AccountNotFoundError(
            "Account does not exist."
        )

    if accounts[account_number]["pin"] != pin:
        raise InvalidPinError(
            "Incorrect PIN."
        )

    return accounts[account_number]


def deposit(account, amount):

    if amount <= 0:
        raise InvalidAmountError(
            "Amount must be greater than zero."
        )

    account["balance"] += amount

    return account["balance"]


def withdraw(account, amount):

    if amount <= 0:
        raise InvalidAmountError(
            "Amount must be greater than zero."
        )

    if amount > account["balance"]:
        raise InsufficientFundsError(
            "Insufficient funds."
        )

    account["balance"] -= amount

    return account["balance"]
