def findPeakElement(nums):
    if len(nums) == 1:
        return 0

    if nums[0] > nums[1]:
        return 0

    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1

    left, right = 1, len(nums) - 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return mid
        elif nums[mid - 1] < nums[mid]:
            left += 1
        else:
            right -= 1

    return None
