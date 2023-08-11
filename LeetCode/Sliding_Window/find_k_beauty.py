def divisorSubstrings(num, k):
    if k == 0:
        return 0

    def isDivisible(divisor):
        return divisor != 0 and num % divisor == 0

    num_str = str(num)
    windowStr = num_str[:k]
    count = 0

    if isDivisible(int(windowStr)):
        count += 1

    for i in range(k, len(num_str)):
        windowStr = windowStr[1:] + num_str[i]
        if isDivisible(int(windowStr)):
            count += 1

    return count
