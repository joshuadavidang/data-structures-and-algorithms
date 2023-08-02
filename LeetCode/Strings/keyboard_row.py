def findWords(words):
    def isValid(word):
        word = word.lower()
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

        for row in rows:
            if all(ch in row for ch in word):
                return True

        return False

    result = []

    for word in words:
        if isValid(word):
            result.append(word)

    return result
