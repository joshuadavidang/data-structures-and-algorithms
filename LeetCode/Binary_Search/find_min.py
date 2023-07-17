# def find_min(nums):
#     result = nums[0]
#     left, right = 0, len(nums) - 1

#     while left <= right:
#         if nums[left] <= nums[right]:
#             result = min(result, nums[left])
#             break

#         mid = (left + right) // 2
#         result = min(result, nums[mid])

#         if nums[mid] > nums[left]:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return result

arr = [1, 2]
if 0 not in arr:
    print("yea")
