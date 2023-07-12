# Solution 1
def contains_duplicate(nums):
    track_data = {}
    for num in nums:
        if num not in track_data:
            track_data[num] = 1
        else:
            track_data[num] += 1

        if track_data[num] >= 2:
            return True

    return not (len(nums) == len(track_data))


# Solution 2
def contains_duplicate(nums):
    track_data = set()
    for num in nums:
        if num in track_data:
            return True
        track_data.add(num)
    return False
