def remove_element(arr, num):
    i = 0
    for j in range(len(arr)):
        if arr[j] != num:
            arr[i] = arr[j]
            i += 1
    return i
