def uniqueMorseRepresentations(words):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    morse_codes = [
        ".-",
        "-...",
        "-.-.",
        "-..",
        ".",
        "..-.",
        "--.",
        "....",
        "..",
        ".---",
        "-.-",
        ".-..",
        "--",
        "-.",
        "---",
        ".--.",
        "--.-",
        ".-.",
        "...",
        "-",
        "..-",
        "...-",
        ".--",
        "-..-",
        "-.--",
        "--..",
    ]
    mapping = {}

    for i, alphabet in enumerate(alphabets):
        mapping[alphabet] = morse_codes[i]

    unique_rep = set()

    for word in words:
        code = ""
        for ch in word:
            if ch in mapping:
                code += mapping[ch]
        unique_rep.add(code)

    return len(unique_rep)
