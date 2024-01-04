def topKFrequent(nums, k):
    mapping = {}
    freq = []
    result = []

    for i in range(len(nums) + 1):
        freq.append([])

    for num in nums:
        if num not in mapping:
            mapping[num] = 1
        else:
            mapping[num] += 1

    for key, value in mapping.items():
        freq[value].append(key)

    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            result.append(num)

            if len(result) == k:
                return result
