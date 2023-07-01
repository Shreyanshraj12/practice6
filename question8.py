def multiply(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    k, n = len(mat2), len(mat2[0])
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        row1 = mat1[i]
        for j in range(n):
            col2 = [mat2[k][j] for k in range(k)]
            dot_product = 0
            for p in range(k):
                val1, val2 = row1[p], col2[p]
                if val1 != 0 and val2 != 0:
                    dot_product += val1 * val2
            result[i][j] = dot_product

    return result
mat1 = [[1, 0, 0],
        [-1, 0, 3]]

mat2 = [[7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]]

print(multiply(mat1, mat2))
