def find_min_insertions_recur(s_list, reg, ins):

    if s_list in reg:
        return reg[s_list] + ins
    st = 0
    ed = len(s_list) - 1
    while st < ed and s_list[st] == s_list[ed]:
        st += 1
        ed -= 1
    if st >= ed:
        return ins
    st_inc = find_min_insertions_recur(s_list[st + 1: ed + 1], reg, ins + 1)
    ed_inc = find_min_insertions_recur(s_list[st: ed], reg, ins + 1)
    reg[s_list] = abs(min(st_inc, ed_inc) - ins)
    return reg[s_list] + ins
    # return min(st_inc, ed_inc)

class Solution:
    def minInsertions(self, s: str) -> int:
        reg = {}
        # s_list = list(s)
        return find_min_insertions_recur(s, reg, 0)


print(Solution().minInsertions("zjj"))
