<h1 align="center">🧩 Sudoku Validator 🧩</h1>

This program serves as my Python solution for the [Problem: Sudoku board Validator on Codewars](https://www.codewars.com/kata/63d1bac72de941033dbf87ae/python).
I found the problem quite intriguing, so I have it as a basic project in this repository!

## Rules of Sudoku[^1]

<img src= "https://sandiway.arizona.edu/sudoku/wildcatjan17p.gif">

> Sample Sudoku Game Board

The Sudoku board consists of a square grid of 9 x 9. 
<br>
In this project we represent the board by 9 lists _(each consisting of 9 elements)_ nested as individual elements in a single list.

3 checks are needed to be made on the board:
1. Each list _(or row)_ must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition. *(i.e. each list's element of the same index must not have repeating digits, yet should have all digits from 1-9)*
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

## `validate_sudoku()`

It creates a set of integers (1-9) which are valid as a solution for any column, row, or sub-box.
Then, it first makes the checks for the 1st rule.

```py
    valid = {1,2,3,4,5,6,7,8,9}
    for row in board:
        if set(row) != valid:
            return False
```

<br>

If the rule is satisfied, then it makes checks for the 2nd rule.

```py
     for i in range(9):
        for j in range(9):
            col.add(board[j][i])
        if col != valid:
            return False
        col.clear()
```

<br>

If the rule is satisfied, then it makes the last checks for the 3rd rule.

```py
    i, j, k = 0, 1, 2
    start = 0
    square = set()
    for rects in range(3):
        for col in range(2, 9, 3):
            square.update(set(board[i][start:col+1]))
            square.update(set(board[j][start:col+1]))
            square.update(set(board[k][start:col+1]))
            if square != valid:
                return False
            start += 3
            square.clear()
        i+=3
        j+=3
        k+=3
        start = 0
    return True
```

If all these checks are passed, it means it is a valid Sudoku solution, and it returns `True`.

<br>
<br>

Check the sample test-cases in the code for a better understanding.

[^1]: If you are new to the game of Sudoku, check this [link](https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/)
