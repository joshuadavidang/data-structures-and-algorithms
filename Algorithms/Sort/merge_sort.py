class DSA:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def sortArray(self, nums):
        n = len(nums)
        if n <= 1:
            return nums

        mid = n // 2
        left_half = nums[:mid]
        right_half = nums[mid:]

        left_half = self.sortArray(left_half)
        right_half = self.sortArray(right_half)

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        i = j = 0
        result = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result


array = [55, 123, 21, 15, 99, 3, 12]
dsa = DSA("algorithm", "merge_sort")
sorted_array = dsa.sortArray(array)
print("Original Array:", array)
print("Sorted Array:", sorted_array)
