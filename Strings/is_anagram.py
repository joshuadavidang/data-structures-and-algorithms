def is_anagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    for char in t:
        if char in freq:
            freq[char] -= 1
            if freq[char] < 0:
                return False
        else:
            return False

    for value in freq.values():
        if value != 0:
            return False

    return True
