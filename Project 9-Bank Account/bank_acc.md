<h1 align='center'>🏦 Bank Account 🏦</h1>

This project consists of a Bank Account program based on the simple concepts of **Object Oriented Programming.**[^1]
> P.S. This project was my first time learning about OOPs concepts :p

We store the accounts created, along with their corresponding details, in the `accounts.csv` file.
We import some modules like `pandas` and `pathlib`. So that to operate upon the `accounts.csv` file.</p>
<br>

## BankAccount Class

First, we declare some _class variables_.

Secondly, we define the `\_\_init__()` function, that is called every time an object is created with the **BankAccount** Class. It assigns values to the attributes of the object.

The class takes two arguments:
- `name`: Name of the account bearer.
- `balance`: Balance at the beginning of the account creation, if not passed, default balance is set to 0.
    - _Note:_ A bonus balance of 1000 is added upon account creation.
<br>
<hr>

### `@classmethods`
#### `instantiateFromStr()`
It takes a string, separate the account name and the account balance (if entered), and then creates the corresponding object.

<br>
<hr>

### `@staticmethods`
#### `newAccountNumber()`
It simply generates a random account number, consisting of an integer digit and an English alphabet. It makes use of the `numwords.py` script in the same directory.

#### `getAccountDetails()`
It simpy fetches the account details of a specific account number passed as an argument.

#### `getAccountHistory()`
It fetches the account history, which has all the operations performed on a particular bank account, whose account number has been passed as an argument.

#### `updateCSV()`
It simply updates the `accounts.csv` file; it is called at the end of every method to update the details of each bank account.

<br>

## Bank Account Operations
#### `deposit()` method
It takes an integer argument, and adds the same sum to the corresponding account's balance.

#### `withdraw()` method
It takes an integer argument, and deducts the same sum from the corresponding account's balance.

#### `invest()` method
It takes an integer argument, and deducts the same sum from the corresponding account's balance.
The second argument is the time in years, the sum compounds over the same period of time, the rate depends on the current balance of the account.

It finally adds the compounded amount to the balance.

#### `transferMoney()` method
It takes an object as an argument, and a sum, it subtracts the same sum from the object passed as the **self** argument, and adds the same sum to the other account.

<br>
<hr>

Apart from these methods, there is the `__repr__()` method, which changes the way the object is represented.

> Check out the sample objects created at the end of the code!
 
[^1]: Check out this page obout [OOPs](https://docs.python.org/3/tutorial/classes.html) in Python.
