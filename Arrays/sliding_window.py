# maximum sum of a subarray of size k

def maxSum(arr, k):
    # find the length of array
    n = len(arr)

    # corner case, if size k is more than the size of array,
    # return -1
    if n < k:
        return -1
    
    # sum of initial window of size k
    initial_window = sum(arr[:k])

    # base case for comparison
    max_sum = initial_window

    # remaining sum
    for i in range(n - k):
        initial_window = initial_window - arr[i] + arr[i + k]
        max_sum = max(initial_window, max_sum)

    return max_sum

arr = [5, 2, -1, 0, 3]
k = 3
print(maxSum(arr, k))

