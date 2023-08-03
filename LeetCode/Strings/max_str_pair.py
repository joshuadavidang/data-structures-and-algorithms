def maximumNumberOfStringPairs(words):
    def reverseString(str):
        str = list(str)
        left, right = 0, len(str) - 1
        while left < right:
            str[left], str[right] = str[right], str[left]
            left += 1
            right -= 1

        return "".join(str)

    mapping = {}
    count = 0

    for word in words:
        reversedWord = reverseString(word)
        if reversedWord not in mapping:
            mapping[word] = 1
        else:
            count += 1

    return count
