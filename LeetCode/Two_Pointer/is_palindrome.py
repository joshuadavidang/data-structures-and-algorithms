def isPalindrome(s):
    updated_str = ""
    for ch in s:
        if ch.isalnum():
            ch = ch.lower()
            updated_str += ch

    query = list(updated_str)
    left, right = 0, len(query) - 1
    while left < right:
        if query[left] != query[right]:
            return False
        left += 1
        right -= 1
    return True
