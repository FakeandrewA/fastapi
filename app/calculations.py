def add(num1: int,num2:int):
    return num1+num2

def subtract(num1:int,num2:int):
    return num1-num2

def multiply(num1:int,num2:int):
    return num1*num2

def divide(num1:int,num2:int):
    return num1/num2

class InsufficientFunds(Exception):
    def __init__(self):
        super().__init__("Insufficent funds in account")

class BankAccount():
    def __init__(self,starting_balance=0):
        self.balance = starting_balance 
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientFunds()
        self.balance -= amount
    def collect_interest(self):
        self.balance *= 1.1
