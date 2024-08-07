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

def sum_odd_and_even(num_arr):
    sum_odd = 0
    sum_even = 0

    for num in num_arr:
        
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    
    return [sum_even, sum_odd]

def format_date(dateStr):
    date_arr = dateStr.split("/")[::-1]
    return "/".join(date_arr)

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

# Problem 4
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

