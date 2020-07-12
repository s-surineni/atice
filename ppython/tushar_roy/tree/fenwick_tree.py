class FenwickTree:
    def __init__(self, arr):
        self.orig_arr = arr
        self.fenwick_len = (len(arr) + 1)
        self.fenwick_tree = [0] * self.fenwick_len

    def construct_fenwick_tree(self):
        for idx in range(1, self.fenwick_len):
            self.update_tree(idx, self.orig_arr[idx - 1])

    def get_parent(self, idx):
        return idx - (-idx & idx)

    def get_next(self, idx):
        return idx + (idx & - idx)

    def find_sum(self, hi):
        hi += 1
        res = 0
        while hi:
            res += self.fenwick_tree[hi]
            hi = self.get_parent(hi)
        return res

    def update_tree(self, idx, val):
        while idx < self.fenwick_len:
            self.fenwick_tree[idx] += val
            idx = self.get_next(idx)

    def range_sum(self, x, y):
        x, y = max(x, y), min(x, y)
        return self.find_sum(x) - self.find_sum(y - 1)


if __name__ == '__main__':
    # arr = [int(i) for i in input().strip().split()]
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    ft = FenwickTree(arr)
    ft.construct_fenwick_tree()
    print(ft.fenwick_tree)
    print(ft.find_sum(4))
    ft.update_tree(1, 4)
    print(ft.fenwick_tree)
    print('range (2, 5)', ft.range_sum(2, 5))
