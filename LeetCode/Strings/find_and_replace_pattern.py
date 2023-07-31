def findAndReplacePattern(words, pattern):
    def getPattern(word):
        mapping = {}
        pattern = []

        for i, ch in enumerate(word):
            if ch not in mapping:
                mapping[ch] = i
            pattern.append(mapping[ch])
        return pattern

    result = []

    for word in words:
        if getPattern(word) == getPattern(pattern):
            result.append(word)

    return result
