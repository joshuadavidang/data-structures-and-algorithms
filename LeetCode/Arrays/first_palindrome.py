def firstPalindrome(words):
    def isPalindrome(word):
        word = list(word)
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1

        return True

    for word in words:
        if isPalindrome(word):
            return word

    return ""
