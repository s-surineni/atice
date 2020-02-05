def flipping_an_image(mat):
    rows = len(mat)
    cols = len(mat[0])
    for ri in range(rows):
        for ci in range(cols // 2):
            mat[ri][ci], mat[ri][cols - ci - 1] = 1 - mat[ri][cols - ci - 1], 1 - mat[ri][ci]

        if cols % 2:
            mat[ri][cols // 2] -= 1
    return mat
