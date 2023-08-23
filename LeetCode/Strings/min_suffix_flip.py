def minFlips(target):
    flips = 0
    currState = "0"

    for ch in target:
        if ch != currState:
            flips += 1
            currState = "1" if currState == "0" else "0"

    return flips
