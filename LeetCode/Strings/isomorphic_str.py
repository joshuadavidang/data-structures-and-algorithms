def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s, map_t = {}, {}

    for i, s_value in enumerate(s):
        if s_value in map_s:
            if map_s[s_value] != t[i]:
                return False
        else:
            map_s[s_value] = t[i]

        if t[i] in map_t:
            if map_t[t[i]] != s_value:
                return False
        else:
            map_t[t[i]] = s_value

    return True
