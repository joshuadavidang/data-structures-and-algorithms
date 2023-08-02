def moveZeros(nums):
    if not nums:
        return

    left, right = 0, 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    return nums
