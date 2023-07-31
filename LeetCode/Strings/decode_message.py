def decodeMessage(key, message):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    mapping = {" ": " "}
    result = ""
    i = 0

    for ch in key:
        if ch not in mapping:
            mapping[ch] = alphabets[i]
            i += 1

    for ch in message:
        if ch in mapping:
            result += mapping[ch]

    return result
