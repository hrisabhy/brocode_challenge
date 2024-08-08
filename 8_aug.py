# 8 aug brocade assignment

# Problem 1
# In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:

# 0 = [ ] is the empty set
# 1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
# 2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
# n = n−1 ∪ [ n−1 ] = ...
# Write a function that receives an integer n and produces the representing set.

# Examples:
# rep_set(0) ➞ []
# rep_set(1) ➞ [[]]
# rep_set(2) ➞ [[], [[]]]
# rep_set(3) ➞ [[], [[]], [[], [[ ]]]]


# Problem 2
# Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.
# Examples:
# remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

# remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

# remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []


# Problem 3
# Create a function that finds the highest integer in the list using recursion.

# Examples:
# find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

# find_highest([0, 12, 4, 87]) ➞ 87


# Problem 4
# Build a function that creates histograms. Every bar needs to be on a new line and its length corresponds to the numbers in the list passed as an argument. The second argument of the function represents the character that needs to be used.

# Examples:
# histogram([1, 3, 4], "#") ➞ "#\n###\n####"

# #
# ###
# ####

# histogram([6, 2, 15, 3], "=") ➞ "======\n==\n===============\n==="

# ======
# ==
# ===============
# ===

# histogram([1, 10], "+") ➞ "+\n++++++++++"

# +
# ++++++++++


# Problem 5
# Write a function that returns a lambda expression, which adds n to its input

# Examples:
# adds1 = adds_n(1)

# adds1(3) ➞ 4
# adds1(5.7) ➞ 6.7

# adds10 = adds_n(10)

# adds10(44) ➞ 54
# adds10(20) ➞ 30


# Solution 1

# def fn(n):
#     if n == 0:
#         return []
#     else:
#         prev_set = fn(n - 1)
#         return prev_set + [prev_set]

# Solution 2

# def remove_letters(arr, string):
#     result = []
#     for char in arr:
#         if not (char in string):
#             result.append(char)
#     return result

# Solution 3

# def fn(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         max_of_rest = fn(lst[1:])
#         return lst[0] if lst[0] > max_of_rest else max_of_rest

# Solution 4:

# def histogram(arr, char):
#     final_str = ""
#     for i in arr:
#         final_str += char * i + "\n"
#     return final_str

# Solution 5:

# def adds_n(n):
#     return lambda x: x + n