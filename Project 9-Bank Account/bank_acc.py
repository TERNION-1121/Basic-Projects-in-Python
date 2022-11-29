import csv
import random
from numWords import *

with open('D:\Shivy\Basic-Projects-in-Python\Project 9-Bank Account\\accounts.csv', 'w', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(['Sn', 'Name', 'Account number', 'Balance'])
sn = 1
class BankAccount():
    account_number = ''
    accountNumberList = ['']
    accounts = {}
    first_time_balance = 1000

    def __init__(self, name, balance = 0):
        global sn
        self.name = name
        self.account_number = BankAccount.newAccountNumber()
        self.balance = balance + BankAccount.first_time_balance

        BankAccount.accountNumberList.append(BankAccount.account_number)
        BankAccount.accounts[self.account_number] = {'name': self.name,
                                                        'accNum': self.account_number,
                                                        'balance': self.balance }
        with open('D:\Shivy\Basic-Projects-in-Python\Project 9-Bank Account\\accounts.csv', 'a', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow([sn, self.name, self.account_number, self.balance])
        sn+=1

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
        self.balance+=sum
        BankAccount.accounts[self.account_number]['balance'] = self.balance
    
    def withdraw(self, sum: int):
        if self.balance == 0 or self.balance < sum:
            print("You cannot withdraw more than your current balance! Try depositing some money first!")
        else:
            self.balance-=sum
            BankAccount.accounts[self.account_number]['balance'] = self.balance

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
        
    def transferMoney(self, acc: object, amt: int):
        self.balance-=amt
        acc.balance+=amt
        BankAccount.accounts[self.account_number]['balance'] = self.balance
        BankAccount.accounts[acc.account_number]['balance']+=amt

    def __repr__(self):
        return f"BankAccount({self.name},{self.account_number},{self.balance})"

obj1 = BankAccount("Vikrant Singh Bhadouriya", 1111)
obj2 = BankAccount("Suvgiya Vishwakarma", 3535)
obj3 = BankAccount("Lakshya Singh Chauhan", 7777)
obj4 = BankAccount("Kushagra Chauhan", 1040)