from bank import BankAccount


def test_deposit_independent():
    account = BankAccount(100)  # Fresh account
    account.deposit(50)
    assert account.balance == 150


def test_withdraw_independent():
    account = BankAccount(100)  # Fresh account
    account.withdraw(30)
    assert account.balance == 70