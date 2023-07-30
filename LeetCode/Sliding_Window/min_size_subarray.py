def minSubArrayLen(target, nums):
    if not nums or sum(nums) < target:
        return 0

    left, curr_sum = 0, 0
    min_length = len(nums) + 1

    for i in range(len(nums)):
        curr_sum += nums[i]

        while curr_sum >= target:
            sliding = i - left + 1
            min_length = min(min_length, sliding)
            curr_sum -= nums[left]
            left += 1

    if min_length <= len(nums):
        return min_length

    return 0
