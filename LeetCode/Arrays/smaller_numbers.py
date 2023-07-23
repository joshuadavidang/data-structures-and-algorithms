def smallerNumbersThanCurrent(nums):
    temp = sorted(nums)
    mapping = {}

    for i, num in enumerate(temp):
        if num not in mapping:
            mapping[num] = i

    result = []

    for num in nums:
        result.append(mapping[num])

    return result
