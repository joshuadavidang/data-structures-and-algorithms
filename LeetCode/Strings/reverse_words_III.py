def reverseWords(s):
    s = s.split()
    result = []

    for element in s:
        element = list(element)
        left, right = 0, len(element) - 1
        while left < right:
            element[left], element[right] = element[right], element[left]
            left += 1
            right -= 1
        result.append("".join(element))

    sentence = ""

    for word in result:
        sentence += " " + word

    return sentence[1:]
