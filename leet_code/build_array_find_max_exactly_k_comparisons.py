# <!note> the cpp solution to this uses mod in more place
# find where all using mod doesn't impact answer
def build_array_max_k_comparisons(ln, ma, ra):
    ways = []

    for i in range(ln + 1):
        len_m = []
        ways.append(len_m)
        for j in range(ma + 1):
            size_m = [0] * (ra + 1)
            # size_m = [1] * (ra + 1)
            len_m.append(size_m)

    for m in range(1, ma + 1):
        ways[1][m][1] = 1

    for l in range(1, ln + 1):
        for m in range(1, ma + 1):
            for r in range(1, ra + 1):
                curr_val = m * ways[l - 1][m][r]

                for m_val in range(1, m):
                    curr_val += ways[l - 1][m_val][r - 1]
                ways[l][m][r] += curr_val

    # print(ways)
    ans = 0
    for m in range(1, ma + 1):
        ans += ways[ln][m][ra]
    return ans % 1000000007

if __name__ == '__main__':
    print(build_array_max_k_comparisons(2, 3, 1))
