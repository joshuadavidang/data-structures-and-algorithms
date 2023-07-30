def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    ch_to_word, word_to_ch = {}, {}

    for i in range(len(pattern)):
        ch = pattern[i]
        word = words[i]

        if ch not in ch_to_word:
            ch_to_word[ch] = word
        elif ch_to_word[ch] != word:
            return False

        if word not in word_to_ch:
            word_to_ch[word] = ch
        elif word_to_ch[word] != ch:
            return False

    return True
