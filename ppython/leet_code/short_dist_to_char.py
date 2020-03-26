def update_distances(dist_arr, idx):
    s_len = len(dist_arr)
    dist_arr[idx] = 0
    l_i, r_i = idx - 1, idx + 1 
    while True:
        not_modified = True
        if l_i >  -1  and (dist_arr[l_i] is None or dist_arr[l_i] > abs(idx - l_i)):
            dist_arr[l_i] = abs(idx - l_i)
            l_i -= 1
            not_modified = False
        # elif S[l_i] < abs(idx - l_i):
        #     S[l_i] = abs(idx - l_i)
        if r_i < s_len and (dist_arr[r_i] is None or dist_arr[r_i] > abs(idx - r_i)):
            dist_arr[r_i] = abs(idx - r_i)
            r_i += 1
            not_modified = False
        if not_modified:
            return

class Solution:
    def shortestToChar(self, S, C):
        dist_arr = [None] * len(S)
        for idx, ch in enumerate(S):
            if ch == C:
                update_distances(dist_arr, idx)
        return dist_arr


print(Solution().shortestToChar("loveleetcode", 'e'))
