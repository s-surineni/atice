class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        s.sort()
        print(s)
        res = []
        while s:
            if s:
                res.append(s[0])
                s.pop(0)
            idx = 0
            s_len = len(s)
            while idx < s_len:
                ch = s[idx]
                if ch != res[-1]:
                    res.append(ch)
                    s.pop(idx)
                    s_len -= 1
                idx += 1
            if s:
                res.append(s.pop())
            
            idx = len(s) - 1
            
            while idx >= 0:
                ch = s[idx]
                if ch != res[-1]:
                    res.append(ch)
                    s.pop(idx)

                idx -= 1 
        return ''.join(res)


Solution().sortString('leetcode')
