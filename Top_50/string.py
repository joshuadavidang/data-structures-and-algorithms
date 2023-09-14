# Top 50 String Problems
# https://www.geeksforgeeks.org/top-50-string-coding-problems-for-interviews/


def reverseStr(word):
    word = list(word)
    left, right = 0, len(word) - 1
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

    return "".join(word)


str = "Hello"
assert reverseStr(str) == "olleH"
