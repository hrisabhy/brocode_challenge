# 9 aug brocade assignment

# Problem 1
# Create a function that, given a number, returns the corresponding value of that index in the Fibonacci series using recursion.
# The Fibonacci Sequence is the series of numbers:

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding the two numbers before it:

# The 2 is found by adding the two numbers before it (1+1).
# The 3 is found by adding the two numbers before it (1+2).
# The 5 is (2+3), and so on!

# Example:
# fibonacci(3) ➞ 3
# fibonacci(7) ➞ 21
# fibonacci(12) ➞ 233

# Solution 1
def fibonacci(n):
    if (n <= 1):
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

# Problem 2
# Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in functions max() and sorted() are prohibited.

# Examples:
# largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
# largest_even([1, 3, 5, 7]) ➞ -1
# largest_even([0, 19, 18973623]) ➞ 0
# Consider using the modulo operator % or the bitwise and operator &.

# Solution 2
def largest_even(arr):
    max_eve = float("-inf")
    for num in arr:
        if num % 2 == 0 and num > max_eve:
            max_eve = num
    if max_eve == float("-inf"):
        return -1
    return max_eve 

# Problem 3
# Write a function that recursively determines if a string is a palindrome.

# Examples:
# is_palindrome("abcba") ➞ True
# is_palindrome("b") ➞ True
# is_palindrome("") ➞ True
# is_palindrome("ad") ➞ False
# An empty string counts as a palindrome.

def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1: -1])
    
# Problem 4
# Create a function that transforms sentences ending with multiple question marks ? or exclamation marks ! into a sentence only ending with one without changing punctuation in the middle of the sentences.

# Examples:
# no_yelling("What went wrong?????????") ➞ "What went wrong?"
# no_yelling("Oh my goodness!!!") ➞ "Oh my goodness!"
# no_yelling("I just!!! can!!! not!!! believe!!! it!!!") ➞ "I just!!! can!!! not!!! believe!!! it!"
# no_yelling("Oh my goodness!") ➞ "Oh my goodness!"
# Only change repeating punctuation at the end of the sentence.

def no_yelling(str):
    ind = -1
    token = str[-1]
    for i in range(len(str) - 1, -1, -1):
        if str[i] != token:
            ind = i
            break
    return str[:ind + 1] + token

# Problem 5
# Given a number, return the total sum of that number multiplied by every number between 1 and 10. Do not use the sum() built-in function.

# Examples:
# multi_sum(1) ➞ 55
# # 1 x 1 + 1 x 2 + 1 x 3 ...... 1 x 9 + 1 x 10 = 55
# multi_sum(6) ➞ 330
# # 6 x 1 + 6 x 2 + 6 x 3 ...... 6 x 9 + 6 x 10 = 330
# multi_sum(10) ➞ 550
# multi_sum(8) ➞ 440
# multi_sum(2) ➞ 110

def multi_sum(num):
    res = 0
    for i in range(1, 11):
        res += i * num
    return res