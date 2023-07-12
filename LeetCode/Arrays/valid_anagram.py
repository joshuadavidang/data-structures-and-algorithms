def valid_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for ch in s:
        if ch not in count_s:
            count_s[ch] = 1
        else:
            count_s[ch] += 1

    for ch in t:
        if ch not in count_t:
            count_t[ch] = 1
        else:
            count_t[ch] += 1

    for ch in count_s:
        if count_s[ch] != count_t.get(ch, 0):
            return False

    return True
