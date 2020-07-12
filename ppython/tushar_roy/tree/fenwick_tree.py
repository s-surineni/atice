class FenwickTree:
    def __init__(self, arr):
        self.orig_arr = arr
        self.fenwick_len = (len(arr) + 1)
        self.fenwick_arr = [0] * self.fenwick_len

    def construct_fenwick_tree(self):
        for idx in range(1, self.fenwick_len):
            nxt_idx = idx
            while nxt_idx < len(self.fenwick_arr):
                self.fenwick_arr[nxt_idx] += self.orig_arr[idx - 1]
                nxt_idx += (nxt_idx & -nxt_idx)

    def find_range_sum(self, hi):
        hi += 1
        res = self.fenwick_arr[hi]
        while hi:
            hi -= (-hi & hi)
            res += self.fenwick_arr[hi]
        return res

    def update_index(self, idx, val):
        diff = val - self.orig_arr[idx]
        self.orig_arr[idx] = val
        nxt_idx = idx + 1
        self.fenwick_arr[idx + 1] = diff

        while nxt_idx < len(self.fenwick_arr):
            self.fenwick_arr[nxt_idx] += diff
            nxt_idx += (nxt_idx & -nxt_idx)


if __name__ == '__main__':
    # arr = [int(i) for i in input().strip().split()]
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    ft = FenwickTree(arr)
    ft.construct_fenwick_tree()
    print(ft.fenwick_arr)
    print(ft.find_range_sum(4))
    ft.update_index(1, 4)
    print(ft.fenwick_arr)
