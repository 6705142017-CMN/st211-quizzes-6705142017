from bank import BankAccount
def test_everything_at_once():
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.deposit(10)
    assert account.balance == 130
    