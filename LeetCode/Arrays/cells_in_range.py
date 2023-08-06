def cellsInRange(s):
    start, end = s.split(":")
    startLetter, startNum = start[0], int(start[-1])
    endLetter, endNum = end[0], int(end[-1])
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    startIndex = alphabets.index(startLetter)
    endIndex = alphabets.index(endLetter)
    alphabetSlice = alphabets[startIndex : endIndex + 1]

    result = []
    for alphabet in alphabetSlice:
        for num in range(startNum, endNum + 1):
            total = alphabet + str(num)
            result.append(total)

    return result
