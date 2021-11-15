    
class Solution:
    def removeDuplicates(self, S: str) -> str:
        s_list = list(S)
        idx = 0
        while True:
            if idx >= 0 and (idx + 1) < len(s_list) and s_list[idx] == s_list[idx + 1]:
                s_list = s_list[:idx] + s_list[idx + 2:]
                idx = idx - 1
            else:
                idx += 1
            if idx + 1 >= len(s_list):
                break

        return ''.join(s_list)



print(Solution().removeDuplicates('abbaca'))