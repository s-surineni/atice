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
                nxt_idx += ((~nxt_idx) + 1)


if __name__ == '__main__':
    # arr = [int(i) for i in input().strip().split()]
    arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    ft = FenwickTree(arr)
    ft.construct_fenwick_tree()
    print(ft.fenwick_arr)
