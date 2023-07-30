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
