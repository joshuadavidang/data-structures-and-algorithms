def evalPostfix(str):
    if not str:
        return 0

    result = []

    for ch in str:
        if ch.isdigit():
            result.append(int(ch))
        else:
            firstNum = result.pop()
            secondNum = result.pop()
            value = calculationHelper(ch, firstNum, secondNum)
            result.append(value)

    return result.pop()


def calculationHelper(op, first, second):
    if op == "+":
        calculation = second + first
    elif op == "-":
        calculation = second - first
    elif op == "*":
        calculation = second * first
    elif op == "/":
        calculation = second / first
    return calculation
