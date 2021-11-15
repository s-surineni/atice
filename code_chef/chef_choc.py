tc = int(input().strip())

for _ in range(tc):
    ro, co, x, y = [int(i) for i in input().strip().split()]
    val1 = y // 2
    if val1 > x:
        val1 = val2 = x
    else:
        val2 = y - val1
    part_cells = (ro * co // 2)
    part_val = part_cells * val1
    part_val += ((ro * co) - part_cells) * val2
    print(part_val)
