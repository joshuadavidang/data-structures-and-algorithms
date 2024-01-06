def maxScore(s):
    zero, one, result = 0, s.count("1"), 0

    for i in range(len(s) - 1):
        if s[i] == "0":
            zero += 1
        else:
            one -= 1

        score = zero + one
        result = max(result, score)

    return result
