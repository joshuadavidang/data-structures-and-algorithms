def romanToInt(s):
    mapping = {}
    symbols = ["I", "V", "X", "L", "C", "D", "M"]
    values = [1, 5, 10, 50, 100, 500, 1000]

    for i, symbol in enumerate(symbols):
        mapping[symbol] = values[i]

    result = 0

    for i, ch in enumerate(s):
        if i < len(s) - 1 and mapping[ch] < mapping[s[i + 1]]:
            result -= mapping[ch]
        else:
            result += mapping[ch]

    return result
