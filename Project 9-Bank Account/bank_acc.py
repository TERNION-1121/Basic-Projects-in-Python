import csv
import random
import pandas
from pathlib import Path
from numWords import *


sn = 1
p = Path(__file__).with_name('accounts.csv') # to open the file in the same directory as the containing module
with open(p, 'w', newline='\n') as file:
                writer = csv.writer(file)
                writer.writerow(['Sn', 'Name', 'Account number', 'Balance'])

class BankAccount():
    account_number = ''
    accountNumberList = ['']
    accounts = {}
    first_time_balance = 1000
    accounts_history = {}

    def __init__(self, name, balance = 0, s = None):
        global sn
        global p
        serialNum = s if s else sn
        self.sn = serialNum-1
        self.name = name
        self.account_number = BankAccount.newAccountNumber()
        self.balance = balance + BankAccount.first_time_balance

        BankAccount.accountNumberList.append(BankAccount.account_number)
        BankAccount.accounts[self.account_number] = {'name': self.name,'accNum': self.account_number,'balance': self.balance }
        BankAccount.accounts_history[self.account_number] = []

        with open(p, 'a', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([sn, self.name, self.account_number, self.balance])
        sn+=1

    @classmethod
    def instantiateFromStr(cls, string):
        if len(string.split('-')) == 2:
            name, balance = string.split('-')
            return cls(name, int(balance))
        else:
            return cls(string.split('-')[0])

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
    
    @staticmethod
    def getAccountHistory(account_num):
        if account_num in BankAccount.accounts_history and len(BankAccount.accounts_history[account_num]) > 0:
            history = BankAccount.accounts_history[account_num]
            for item in history:
                print(item)
        elif len(BankAccount.accounts_history[account_num]) == 0:
            print('No operations had been performed on this bank account!')
        else:
            print("Please enter a valid account number!")

    @staticmethod
    def updateCSV(*args):
            global p
            df = pandas.read_csv(p)
            obj1 = args[0]
            df.loc[obj1.sn, "Balance"] = obj1.balance
            if len(args) == 2:
                obj2 = args[1]
                df.loc[obj2.sn, "Balance"] = obj2.balance
            df.to_csv(p, index=False)

    def deposit(self, sum: int):
        self.balance+=sum

        BankAccount.accounts[self.account_number]['balance'] = self.balance
        BankAccount.accounts_history[self.account_number].append(f'{sum} was deposited')

        BankAccount.updateCSV(self)

    def withdraw(self, sum: int):
        if self.balance == 0 or self.balance < sum:
            print("You cannot withdraw more than your current balance! Try depositing some money first!")
        else:
            self.balance-=sum

            BankAccount.accounts[self.account_number]['balance'] = self.balance
            BankAccount.accounts_history[self.account_number].append(f'{sum} was withdrawed')

            BankAccount.updateCSV(self)

    def invest(self, sum: int, time: int):
        if self.balance == 0 or self.balance < sum:
            print("You cannot invest a sum more than your current balance! Try depositing some money first!")
        else:
            if self.balance <= 10000:
                rate = 2.5
            elif self.balance > 10000 and self.balance <=12000:
                rate = 5
            elif self.balance > 12000 and self.balance <= 14000:
                rate = 7.5
            elif self.balance > 14000 and self.balance <= 16000:
                rate = 10
            elif self.balance > 16000 and self.balance <= 18000:
                rate = 12.5
            else:
                rate = 15
            amount = sum * ((1+(rate/1))**time) # compounding
            self.balance+=amount

            BankAccount.accounts[self.account_number]['balance'] = self.balance
            BankAccount.accounts_history[self.account_number].append(f'{sum} was invested, return on investment was {amount}')

            BankAccount.updateCSV(self)
        
    def transferMoney(self, acc: object, amt: int):
        self.balance-=amt
        acc.balance+=amt
        BankAccount.accounts[self.account_number]['balance'] = self.balance
        BankAccount.accounts[acc.account_number]['balance']+=amt
        BankAccount.accounts_history[self.account_number].append(f'{amt} was transferred to {acc.name}')
        BankAccount.accounts_history[acc.account_number].append(f'{amt} was transferred to you by {self.name}')

        BankAccount.updateCSV(self, acc)

    def __repr__(self):
        return f"BankAccount({self.name},{self.account_number},{self.balance})"


obj1 = BankAccount("Vikrant Singh Bhadouriya", 1111)
obj2 = BankAccount("Suvigya Vishwakarma", 3535)
obj3 = BankAccount("Lakshya Singh Chauhan", 7777)
obj4 = BankAccount("Kushagra Chauhan", 1040)
obj5 = BankAccount.instantiateFromStr("Soumil Sachan-1221")
obj6 = BankAccount.instantiateFromStr("Shashank Priye Tripathi")
obj7 = BankAccount.instantiateFromStr("Shiven Sharma-4646")