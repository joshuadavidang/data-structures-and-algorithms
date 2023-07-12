from collections import defaultdict


def group_anagram(strs):
    dict_data = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        dict_data[key].append(word)

    result = []
    for value in dict_data.values():
        result.append(value)

    return result
