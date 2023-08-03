def replaceDigits(s):
    def shift(c, x):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        mapping = {}

        for i in range(len(alphabets)):
            mapping[alphabets[i]] = i + 1

        reversedMapping = {}

        for key, value in mapping.items():
            reversedMapping[value] = key

        return reversedMapping[mapping[c] + x]

    result = ""

    for i in range(len(s)):
        if i % 2 == 1:
            replacement = shift(s[i - 1], int(s[i]))
            result += str(replacement)
        else:
            result += s[i]

    return result
