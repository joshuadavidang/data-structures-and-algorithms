def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    char_to_word, word_to_char = {}, {}

    for i in range(len(pattern)):
        char = pattern[i]
        word = words[i]

        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True
