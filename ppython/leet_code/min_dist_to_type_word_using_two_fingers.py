def find_dist(c1, c2):
    if c1 is None:
        return 0
    idx1 = ord(c1) - ord('A')
    idx2 = ord(c2) - ord('A')
    x1, y1 = idx1 // 26, idx1 % 26
    x2, y2 = idx2 // 26, idx2 % 26
    return abs(x1 - x2) + abs(y1-y2)


def find_min_dist_by_two_fingers(word, pos, c1, c2, vals):
    if pos >= len(word):
        return 0
    pos1 = 0 if c1 is None else ord(c1) - ord('A')
    pos2 = 0 if c2 is None else ord(c2) - ord('A')

    # print('*' * 80)
    # print('iron man c1, c2, pos', c1, c2, pos)

    pos_idx = ord(word[0]) - ord('A')

    if not vals[pos1][pos2][pos]:
        vals[pos1][pos2][pos] = min(find_dist(c1, word[pos])
                                    + find_min_dist_by_two_fingers(word,
                                                                   pos + 1,
                                                                   word[pos],
                                                                   c2, vals),
                                    find_dist(c2, word[pos])
                                    + find_min_dist_by_two_fingers(word,
                                                                   pos + 1,
                                                                   c1,
                                                                   word[pos],
                                                                   vals))
    return vals[pos1][pos2][pos] - 1


class Solution:
    def minimumDistance(self, word):
        vals = []
        word_len = len(word)
        for idx in range(27):
            first = []
            for idx in range(27):
                second = [0] * (word_len + 1)
                first.append(second)
            vals.append(first)
        # print(vals)
        res = find_min_dist_by_two_fingers(word, 0, None, None, vals)
        # print(vals)
        return res


print(Solution().minimumDistance('CAKE'))
