def find_min(nums):
    result = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        if nums[left] <= nums[right]:
            result = min(result, nums[left])
            return result

        mid = (left + right) // 2
        if nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1

        result = min(result, nums[mid])

    return result
