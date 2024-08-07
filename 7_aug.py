# Daily codebro assignment 

# Problem 1
# Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

# Examples: 
# sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# # 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9
# sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])


# Problem 2
# Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

# Example: 
# format_date("11/12/2019") ➞ "20191211"


# Problem 3
# Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. 
# Items of the same value should be in the same sublist.

# Examples:
# advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
# advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]

# Problem 4
# #This I have never solved I am also going to solve this in evening 
# Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X", "O", or a "Draw", 
# where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.

# Examples:
# tic_tac_toe([
#   ["X", "O", "X"],
#   ["O", "X",  "O"],
#   ["O", "X",  "X"]
# ]) ➞ "X"

# tic_tac_toe([
#   ["O", "O", "O"],
#   ["O", "X", "X"],
#   ["E", "X", "X"]
# ]) ➞ "O"

# tic_tac_toe([
#   ["X", "X", "O"],
#   ["O", "O", "X"],
#   ["X", "X", "O"]
# ]) ➞ "Draw"


# Problem 5
# In BlackJack, cards are counted with -1, 0, 1 values:
# 2, 3, 4, 5, 6 are counted as +1
# 7, 8, 9 are counted as 0
# 10, J, Q, K, A are counted as -1
# Create a function that counts the number and returns it from the list of cards provided.

# Examples:
# count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1
# count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6
# count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5

from collections import defaultdict

# Solution 1
def sum_odd_and_even(num_arr):
    sum_odd = 0
    sum_even = 0

    for num in num_arr:
        
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return [sum_even, sum_odd]

# Solution 2
def format_date(dateStr):
    date_arr = dateStr.split("/")[::-1]
    return "/".join(date_arr)

# Solution 3
def advanced_sort(arr):
    hashMap = defaultdict(list)
    res = []
    for num in arr:
        if num in hashMap:
            hashMap[num].append(num)
        else:
            hashMap[num].append(num)
    
    for subArr in hashMap.values():
        res.append(subArr)
    
    return res

# Solution 4
def tic_tac_toe(matArr):

    # Very bad code, I will be revamping this in the evening

    # score_X = 0
    # score_O = 0

    def checkCol(matArr):
        for col in range(3):
            #print(f"Print col {col}")
            score_X = 0
            score_O = 0
            for row in range(3):
                if matArr[row][col] == "X":
                    score_X += 1
                elif matArr[row][col] == "O":
                    score_O += 1
                elif matArr[row][col] == "E" and score_X == 2:
                    return "X"
                elif matArr[row][col] == "E" and score_O == 2:
                    return "O"
                if score_X == 3:
                    return "X"
                elif score_O == 3:
                    return "O"
                elif score_O == score_X:
                    return "Draw"
    
    def checkRow(matArr):
        for row in range(3):
            #print(f"Print row {row}")
            score_X = 0
            score_O = 0
            for col in range(3):
                if matArr[row][col] == "X":
                    score_X += 1
                elif matArr[row][col] == "O":
                    score_O += 1
                elif matArr[row][col] == "E" and score_X == 2:
                    return "X"
                elif matArr[row][col] == "E" and score_O == 2:
                    return "O"
                if score_X == 3:
                    return "X"
                elif score_O == 3:
                    return "O"
                elif score_O == score_X:
                    return "Draw"
    
    def checkDiag(matArr):
        score_X = 0
        score_O = 0
        for i in range(3):
            if matArr[i][i] == "X":
                score_X += 1
                if score_X == 3:
                    return "X"
            elif matArr[i][i] == "O":
                score_O += 1
                if score_O == 3:
                    return "O"
            
            else:
                if score_X == 2:
                    return "X"
                elif score_O == 2:
                    return "O"

    def check_winner(results):
        for result in results:
            if result == "X" or result == "O":
                return result
        if all(result in ["Draw", None] for result in results):
            return "Draw"
        return None
    
    col_results = checkCol(matArr)
    row_results = checkRow(matArr)
    diag_results = checkDiag(matArr)
    
    return check_winner([col_results, row_results, diag_results])