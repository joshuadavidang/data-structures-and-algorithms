class DSA:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def binary_search(self, data, target):
        left, right = 0, len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] > target:
                right = mid - 1          
            elif data[mid] < target:
                left = mid + 1
            else:
                return mid
    
array = [1, 3, 5, 7, 11, 23, 35, 55, 56, 61, 33]
dsa = DSA("algorithm", "binary_search")
index = dsa.binary_search(array, 5)
print("Target found at index:", index)
