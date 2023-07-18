def longest_consecutive(nums):
    # remove any duplicates
    numSet = set(nums)
    longest = 0

    for num in nums:
        if (num - 1) not in numSet:
            # current num is the start of a sequence
            length = 0
            while (num + length) in numSet:
                length += 1
            if length > longest:
                longest = length
    return longest
