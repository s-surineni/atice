def check_if_toepliz(matr):
    diag_map = {}
    for rid, row in enumerate(matr):
        for cid, ele in enumerate(row):
            slot_val = diag_map.get(rid - cid)
            if slot_val != None:
                if slot_val != matr[rid][cid]:
                    return False
            else:
                diag_map[rid - cid] = matr[rid][cid]
    return True


# matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
# matrix = [[1, 2], [2, 2]]
matrix = [[0, 33, 98], [34, 22, 33]]
print(check_if_toepliz(matrix))
