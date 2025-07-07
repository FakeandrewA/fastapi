import pytest
from app.calculations import add,subtract,multiply,divide,BankAccount,InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected",[
    (3,2,5),
    (7,1,8),
    (12,4,16)
])
def test_add(num1,num2,expected):
    """Testing the add function"""
    print(test_add.__doc__)
    assert add(num1,num2)==expected

def test_subtract():
    """Testing the subtract function"""
    print(test_add.__doc__)
    assert subtract(8,5)==3

def test_multiply():
    """Testing the multiply function"""
    print(test_add.__doc__)
    assert multiply(5,8)==40

def test_divide():
    """Testing the divide function"""
    print(test_add.__doc__)
    assert divide(20,5)==4 

def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    bank_account = zero_bank_account
    assert bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected",[
    (3,2,1),
    (7,1,6),
    (12,4,8),
])
def test_bank_transaction(zero_bank_account,deposited,withdrew,expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected

def test_insufficent_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(499)
