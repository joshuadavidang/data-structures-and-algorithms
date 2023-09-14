# Top 50 Recursion Coding Problems for Interviews
# https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/


def printNo(n):
    """
    You are given an integer N. Print numbers from N to 1 without the help of loops.
    Input: N = 5
    Output: 5 4 3 2 1
    """

    if n > 0:
        print(n, end=" ")
        printNo(n - 1)


def findSum(arr):
    """
    arr = [1, 2, 3]
    result = 6
    """

    if len(arr) == 1:
        return arr[0]

    lastElement = arr.pop()
    return lastElement + findSum(arr)


data = [1, 2, 3]
assert findSum(data) == 6


def reverseString(str):
    """
    Write a recursive function to print the reverse of a given string.
    """
    if len(str) == 1:
        return str[0]

    str = list(str)
    lastElement = str.pop()
    return lastElement + reverseString(str)


data = "Hello World"
assert reverseString(data) == "dlroW olleH"


def coinChange(arr, n, sum):
    """
    Given an integer array of coins[] of size N representing different types of denominations and an integer sum,
    the task is to find the number of ways to make sum by using different denominations.

    Input: sum = 4, coins[] = [1, 2, 3]
    Output: 4
    Explanation: there are four solutions: [1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3]
    """

    if sum == 0:
        return 1

    if sum < 0:
        return 0

    if n == 0:
        return 0

    return coinChange(arr, n - 1, sum) + coinChange(arr, n, sum - arr[n - 1])


assert coinChange([1, 2, 3], 3, 4) == 4


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


assert factorial(3) == 6


def recurSum(n):
    if n == 1:
        return 1

    return n + recurSum(n - 1)


assert recurSum(6) == 21


def calculateLength(str):
    if len(str) == 0:
        return 0

    return 1 + calculateLength(str[1:])


str = "Hello"
assert calculateLength(str) == 5


def isPalindrome(word):
    """
    Given a string, write a recursive function that checks if the given string is a palindrome, else, not a palindrome.
    """

    word = word.replace(" ", "").lower()

    if len(word) == 0 or len(word) == 1:
        return True

    if word[0] != word[-1]:
        return False

    return isPalindrome(word[1:-1])


word = "madam"
assert isPalindrome(word) == True


def findMin(arr, n):
    if n == 1:
        return arr[0]

    result = min(arr[n - 1], findMin(arr, n - 1))
    return result


data = [5, -1, 0, 3, 4, -22, 3, 4]
assert findMin(data, len(data)) == -22
