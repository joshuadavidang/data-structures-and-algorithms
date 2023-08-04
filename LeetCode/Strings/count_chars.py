def countCharacters(words, chars):
    def mapCount(mapping, str):
        mapping = {}
        for ch in str:
            if ch not in mapping:
                mapping[ch] = 1
            else:
                mapping[ch] += 1
        return mapping

    chars_map = mapCount({}, chars)
    total_sum = 0

    for word in words:
        word_map = mapCount({}, word)
        is_good_str = True
        for key, value in word_map.items():
            if key not in chars_map or value > chars_map[key]:
                is_good_str = False
                break

        if is_good_str:
            total_sum += len(word)

    return total_sum
