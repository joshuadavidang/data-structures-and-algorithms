def freqAlphabets(s):
    mapping = {}
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(alphabets)):
        mapping[str(i + 1)] = alphabets[i]

    result = ""
    i = 0

    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == "#":
            key = s[i : i + 2]
            result += mapping[key]
            i += 3
        else:
            key = s[i]
            result += mapping[key]
            i += 1

    return result
