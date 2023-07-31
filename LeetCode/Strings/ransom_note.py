def canConstruct(ransomNote, magazine):
    ransom_freq, map_freq = {}, {}

    for note in ransomNote:
        if note not in ransom_freq:
            ransom_freq[note] = 1
        else:
            ransom_freq[note] += 1

    for mag in magazine:
        if mag not in map_freq:
            map_freq[mag] = 1
        else:
            map_freq[mag] += 1

    for key, value in ransom_freq.items():
        if key not in map_freq or map_freq[key] < value:
            return False

    return True
