def is_palindrome(str):
    str = list(str)
    l, r = 0, len(str) - 1
    while l < r:
        if str[l] != str[r]:
            return False
        l += 1
        r -= 1

    return True
