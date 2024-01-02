def makeEqual(words):
    mapping = {}

    for word in words:
        for ch in word:
            if ch not in mapping:
                mapping[ch] = 1
            else:
                mapping[ch] += 1

    for value in mapping.values():
        if value % len(words) > 0:
            return False

    return True
