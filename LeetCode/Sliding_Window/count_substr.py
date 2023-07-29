def countGoodSubstrings(s):
    k = 3
    if len(s) < k:
        return 0

    result = []
    windowStr = s[:k]
    result.append(windowStr)

    for i in range(k, len(s)):
        windowStr = windowStr[1:] + s[i]
        result.append(windowStr)

    counter = 0

    for element in result:
        if len(set(element)) == k:
            counter += 1

    return counter
