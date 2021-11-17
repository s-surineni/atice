def rotate_image(matrix):
    mlen = len(matrix)
    for rid, row in enumerate(matrix):
        for cid in range(rid, mlen):
            matrix[rid][cid], matrix[cid][rid] = matrix[cid][rid], matrix[rid][cid]
    for rid in range(mlen):
        for cid in range(mlen // 2):
            matrix[rid][cid], matrix[rid][-cid - 1] = (
                matrix[rid][-cid - 1],
                matrix[rid][cid],
            )
    print(matrix)


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(rotate_image(matrix))
print(matrix)
