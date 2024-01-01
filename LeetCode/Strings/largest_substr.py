def maxLengthBetweenEqualCharacters(s):
    mapping = {}
    result = -1

    for i, ch in enumerate(s):
        if ch not in mapping:
            mapping[ch] = i
        else:
            result = max(result, i - mapping[ch] - 1)

    return result
