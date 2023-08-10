def numberOfSubarrays(nums, k):
    left = 0
    oddCount = 0
    count = 0
    result = 0

    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            oddCount += 1
            count = 0

        while oddCount == k:
            if nums[left] % 2 == 1:
                oddCount -= 1
            left += 1
            count += 1

        result += count

    return result
