def threeSum(nums):
    result = []
    nums.sort()

    for i, num in enumerate(nums):
        if i > 0 and nums[i - 1] == num:
            continue

        left, right = i + 1, len(nums) - 1
        while left < right:
            threeSum = num + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                result.append([num, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
    return result
