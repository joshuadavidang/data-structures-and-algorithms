class DSA:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def binary_search(self, books, target):
        left, right = 0, len(books) - 1
        while left <= right:
            mid = (left + right) // 2
            if books[mid] > target:
                right = mid - 1
            elif books[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
