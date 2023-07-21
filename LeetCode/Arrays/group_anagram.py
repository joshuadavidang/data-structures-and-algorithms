def group_anagram(strs):
    dict_data = {}

    for word in strs:
        sorted_word = sorted(word)
        key = "".join(sorted_word)
        if key not in dict_data:
            dict_data[key] = []

        dict_data[key].append(word)

    result = []
    for values in dict_data.values():
        result.append(values)

    return result
