def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_map, t_map = {}, {}

    for i, s_val in enumerate(s):
        if s_val not in s_map:
            s_map[s_val] = t[i]

        elif s_map[s_val] != t[i]:
            return False

        if t[i] not in t_map:
            t_map[t[i]] = s_val

        elif t_map[t[i]] != s_val:
            return False

    return True


def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s, map_t = {}, {}
    s_result = []
    t_result = []

    for i, ch in enumerate(s):
        if ch not in map_s:
            map_s[ch] = i
        s_result.append(map_s[ch])

    for i, ch in enumerate(t):
        if ch not in map_t:
            map_t[ch] = i
        t_result.append(map_t[ch])

    return s_result == t_result
