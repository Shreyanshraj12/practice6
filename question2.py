def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    start, end = 0, m * n - 1

    while start <= end:
        mid = (start + end) // 2
        row, col = mid // n, mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False
