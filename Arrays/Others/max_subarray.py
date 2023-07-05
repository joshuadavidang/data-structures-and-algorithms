def max_subarray(arr):
    if len(arr) == 0:
        return []

    maxSum = arr[0]
    currentSum = arr[0]

    for i in range(1, len(arr)):
        if currentSum < 0:
            currentSum = arr[i]
        else:
            currentSum += arr[i]

        if currentSum > maxSum:
            maxSum = currentSum
        
    return maxSum