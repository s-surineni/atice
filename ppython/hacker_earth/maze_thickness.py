def maze_traveller_bt(threshold, initThickness, rate, rows, cols, row, col, day):
    if (row, col) == (rows - 1, cols - 1):
        # print('YES')
        return 'YES'
    if row < rows and col < cols:
        res = False
        # print('row col', row, col, rows, cols)
        
        if col + 1 < cols and initThickness[row][col + 1] + day <= threshold:
            
            res = maze_traveller_bt(threshold, initThickness, rate, rows, cols, row, col + 1, day + 1)
        if not res and row + 1 < rows and initThickness[row + 1][col] + day <= threshold:
            res = maze_traveller_bt(threshold, initThickness, rate, rows, cols, row + 1, col, day + 1)
        print('row col res', row, col, res)
        return res
    
def mazeTraveller (threshold, initThickness, rate, rows, cols):
    # print('initThickness', initThickness)
    res = maze_traveller_bt(threshold, initThickness, rate, rows, cols, 0, 0, 1)
    if not res:
        return 'NO'
    return
    

T = int(input())
for _ in range(T):
    rows, cols, threshold = map(int, input().split(' '))
    initThickness = []
    for _ in range(rows):
        initThickness.append(list(map(int, input().split(' '))))
    rate = []
    for _ in range(rows):
        rate.append(list(map(int, input().split(' '))))

    out_ = mazeTraveller(threshold, initThickness, rate, rows, cols)
    print(out_)
