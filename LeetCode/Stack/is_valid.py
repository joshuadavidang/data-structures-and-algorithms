def is_valid(s):
    result = []
    dict_data = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in dict_data:
            if result and result[-1] == dict_data[ch]:
                result.pop()
        else:
            result.append(ch)

    return len(result) == 0
