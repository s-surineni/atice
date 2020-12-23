# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/
import collections


def minFlips(mat):
    m, n = len(mat), len(mat[0])
    start = sum(cell << (i * n + j) for i, row in enumerate(mat)
                for j, cell in enumerate(row))
    print('*' * 80)
    print('iron man start', start)
    dq = collections.deque([(start, 0)])
    print('*' * 80)
    print('iron man dq', dq)
    seen = {start}
    while dq:
        cur, step = dq.popleft()
        print('*' * 80)
        print('iron man cur, step', cur, step)
        if not cur:
            return step
        print('*' * 80)
        for i in range(m):
            for j in range(n):
                next = cur
                print('*' * 80)
                print('iron man next 1', next)
                print('iron man i, j', i, j)
                for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1,
                                                                         j):
                    if m > r >= 0 <= c < n:
                        print('iron man r, c', r, c, end=' ')
                        next ^= 1 << (r * n + c)
                print()
                if next not in seen:
                    print('*' * 80)
                    print('iron man next 2', next)
                    seen.add(next)
                    dq.append((next, step + 1))
    print('*' * 80)
    print('iron man seen', seen)
    print('*' * 80)
    print('iron man step', step)
    return -1


# minFlips([[0], [1]])
# minFlips([[1], [0]])
minFlips([[0], [0], [1]])
