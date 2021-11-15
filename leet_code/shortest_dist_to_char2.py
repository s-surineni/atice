class Solution:
    def shortestToChar(self, S, C):
        s_len = len(S)
        dist_arr = [float('inf')] * s_len
        c_idx = float('inf')

        for idx, ch in enumerate(S):
            if ch == C:
                c_idx = idx
            dist_arr[idx] = min(dist_arr, abs(c_idx - idx))

        c_idx = float('inf')
        for idx in range(s_len - 1, -1, -1):
            if S[idx] == C:
                c_idx = idx
            dist_arr[idx] = min(dist_arr, abs(c_idx - idx))
        return dist_arr
