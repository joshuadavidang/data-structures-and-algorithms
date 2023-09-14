# Top 50 Stack Problems
# https://www.geeksforgeeks.org/top-50-problems-on-stack-data-structure-asked-in-interviews/


def reverseStr(str):
    """
    Given a string, reverse it using stack.
    """

    stack = []
    result = ""

    for ch in str:
        stack.append(ch)

    while stack:
        result += stack.pop()

    return result


assert reverseStr("Hello") == "olleH"


def isValid(brackets):
    mapping = {"}": "{", ")": "(", "]": "["}
    stack = []

    for bracket in brackets:
        if bracket not in mapping:
            stack.append(bracket)
        else:
            if stack and stack[-1] == mapping[bracket]:
                stack.pop()
            else:
                return False

    return True if not stack else False


data = "[()]{}{[()()]()}"
assert isValid(data) == True


def reverseArr(data):
    stack = []
    for element in data:
        stack.append(element)

    result = []

    while stack:
        result.append(stack.pop())

    return result


arr = [1, 5, 7, 12, 15]
assert reverseArr(arr) == [15, 12, 7, 5, 1]


def reverseStr(word):
    stack = []
    for ch in word:
        stack.append(ch)

    result = ""
    while stack:
        result += stack.pop()

    return result


str = "Hello"
assert reverseStr(str) == "olleH"


def evaluateStr(str):
    """
    Evaluation of Postfix Expression
    """

    if len(str) == 0:
        return 0

    stack = []

    for ch in str:
        if ch.isdigit():
            num = int(ch)
            stack.append(num)
        else:
            firstNum = stack.pop()
            secondNum = stack.pop()
            value = calculationHelper(ch, firstNum, secondNum)
            stack.append(value)

    return stack.pop()


def calculationHelper(op, firstDigit, secondDigit):
    if op == "+":
        calculation = secondDigit + firstDigit
    elif op == "-":
        calculation = secondDigit - firstDigit
    elif op == "*":
        calculation = secondDigit * firstDigit
    elif op == "/":
        calculation = secondDigit / firstDigit
    return calculation


str = "84-"
assert evaluateStr(str) == 4
