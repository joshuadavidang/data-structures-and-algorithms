def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    top, bot = 0, rows - 1

    while top <= bot:
        mid = (top + bot) // 2
        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bot = mid - 1
        else:
            break

    if not (top <= bot):
        return False

    row = (top + bot) // 2
    left, right = 0, cols - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] < target:
            left = mid + 1
        elif matrix[row][mid] > target:
            right = mid - 1
        else:
            return True

    return False
