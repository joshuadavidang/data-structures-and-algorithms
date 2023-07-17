def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # left sorted position
        if nums[left] <= nums[mid]:
            if nums[mid] < target or nums[left] > target:
                # ignore left, move towards right
                left = mid + 1
            else:
                # ignore right, move towards left
                right = mid - 1

        # right sorted position
        else:
            if nums[mid] > target or nums[right] < target:
                right = mid - 1
            else:
                left = mid + 1

    return -1
