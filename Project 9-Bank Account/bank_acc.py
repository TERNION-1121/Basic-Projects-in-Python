import random
from numWords import *

# add an investment method!
class BankAccount():
    account_number = ''
    accountNumberList = ['']
    accounts = {}
    first_time_balance = 1000

    def __init__(self, name, balance = 0):
        self.name = name
        self.account_number = BankAccount.newAccountNumber()
        self.balance = balance + BankAccount.first_time_balance

        BankAccount.accountNumberList.append(BankAccount.account_number)
        BankAccount.accounts[self.account_number] = {'name': self.name,
                                                        'accNum': self.account_number,
                                                        'balance': self.balance }
    @staticmethod
    def newAccountNumber():
        while BankAccount.account_number in BankAccount.accountNumberList:
            BankAccount.account_number = random.choice(numbers) + random.choice(words)
        return BankAccount.account_number

    @staticmethod
    def getAccountDetails(account_num):
        '''Enter your account number as the argument'''
        if account_num in BankAccount.accountNumberList:
            tempDetails = BankAccount.accounts[account_num]
            print(f"Account Bearer: {tempDetails['name']}\nAccount Number: {tempDetails['accNum']}\nAccount Balance: {tempDetails['balance']}")
        else:
            print("Please enter a valid account number!")

    def deposit(self, sum: int):
        self.balance = self.balance + sum
        BankAccount.accounts[self.account_number]['balance'] = self.balance
    
    def withdraw(self, sum: int):
        if self.balance == 0 or self.balance < sum:
            print("You cannot withdraw more than your current balance! Try depositing some money first!")
        else:
            self.balance-=sum
            BankAccount.accounts[self.account_number]['balance'] = self.balance

    def invest(self, sum: int, time: int):
        self.balance-=sum
        rate = 10
        amount = sum * ((1+(rate/1))**time)
        self.balance+=amount
        BankAccount.accounts[self.account_number]['balance'] = self.balance
        
    def transferMoney(self, accNo, amt):
        self.balance-=amt
        BankAccount.accounts[self.account_number]['balance'] = self.balance
        BankAccount.accounts[accNo]['balance']+=amt

    def __repr__(self):
        return f"BankAccount({self.name},{self.account_number},{self.balance})"

myAcc = BankAccount('Vikrant Singh Bhadouriya')
num = myAcc.account_number
BankAccount.getAccountDetails(num)