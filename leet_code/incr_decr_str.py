from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        s = sorted(list(s))
        counter_s = Counter(s)
        print(counter_s)
        unique_ch = sorted(list(set(list(s))))
        res = []
        appended = True
        while appended:
            appended = False
            for ch in unique_ch:
                if counter_s[ch] != 0:
                    res.append(ch)
                    appended = True
                    counter_s[ch] -= 1
                    
            for ch in unique_ch[::-1]:
                if counter_s[ch] != 0:
                    res.append(ch)
                    appended = True
                    counter_s[ch] -= 1
            print(counter_s)
        return ''.join(res)


print(Solution().sortString("aaaabbbbcccc"))
