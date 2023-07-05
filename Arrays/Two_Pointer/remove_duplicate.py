def remove_duplicates(nums):
    dict_data = {}
    i = 0

    for j in range(len(nums)):
        if nums[j] not in dict_data:
            dict_data[nums[j]] = 1
        else:
            dict_data[nums[j]] += 1

        if dict_data[nums[j]] == 1:
            nums[i] = nums[j]
            i += 1
        
    return i