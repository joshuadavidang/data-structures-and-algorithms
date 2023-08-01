def findAnagrams(s, p):
    if len(p) > len(s):
        return []

    p_count, s_count = {}, {}

    for i in range(len(p)):
        if p[i] not in p_count:
            p_count[p[i]] = 1
        else:
            p_count[p[i]] += 1

        if s[i] not in s_count:
            s_count[s[i]] = 1
        else:
            s_count[s[i]] += 1

    result = []
    if s_count == p_count:
        result.append(0)

    left = 0
    k = len(p)

    for right in range(k, len(s)):
        s_count[s[left]] -= 1
        if s_count[s[left]] == 0:
            s_count.pop(s[left])

        if s[right] not in s_count:
            s_count[s[right]] = 1
        else:
            s_count[s[right]] += 1

        left += 1

        if s_count == p_count:
            result.append(left)

    return result
