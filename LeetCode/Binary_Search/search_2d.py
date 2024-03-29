def search_matrix(matrix, target):
    top, bot = 0, len(matrix) - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            # ignore top
            top = row + 1
        elif target < matrix[row][0]:
            # ignore bot
            bot = row - 1
        else:
            break

    if not (top <= bot):
        return False

    row = (top + bot) // 2
    left, right = 0, len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        if target > matrix[row][mid]:
            # ignore left
            left = mid + 1
        elif target < matrix[row][mid]:
            # ignore right
            right = mid - 1
        else:
            return True

    return False
