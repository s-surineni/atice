def find_nth_ugly_num(nth):
    mem = [0] * (nth + 1)
    mem[0] = 1
    i2 = i3 = i5 = 0
    n2 = 2
    n3 = 3
    n5 = 5
    pos = 1

    while pos <= nth:
        next_ugly = min(n2, n3, n5)
        mem[pos] = next_ugly

        if next_ugly == n2:
            i2 += 1
            n2 = mem[i2] * 2
        if next_ugly == n3:
            i3 += 1
            n3 = mem[i3] * 3
        if next_ugly == n5:
            i5 += 1
            n5 = mem[i5] * 5
        pos += 1
    return mem


print(find_nth_ugly_num(10))
