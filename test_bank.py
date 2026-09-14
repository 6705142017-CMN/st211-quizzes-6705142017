from bank import BankAccount

def test_deposit_increases_balance():
    account = BankAccount(100)
    new_balance= account.deposit(50)
    assert new_balance == 150
