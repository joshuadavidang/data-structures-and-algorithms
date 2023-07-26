def sortSentence(s):
    sentence = s.split()
    mapping = {}

    for word in sentence:
        index = int(word[-1])
        wordOnly = word[:-1]
        mapping[index] = wordOnly

    result = []

    for i in range(1, len(sentence) + 1):
        result.append(mapping[i])

    return " ".join(result)
