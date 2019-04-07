class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len = len(s)
        dup_dict = {}
        sub_len = 0
        outer = 0
        inner = 0
        curr_sub_len = 0
        while inner < s_len:
            while inner < s_len:
                if s[inner] not in dup_dict:
                    dup_dict[s[inner]] = [inner]
                    curr_sub_len += 1
                    inner += 1
                else:
                    if outer > dup_dict[s[inner]][-1]:
                        dup_dict[s[inner]].append(inner)
                        curr_sub_len += 1
                        inner += 1
                    else:
                        outer = dup_dict[s[inner]][-1] + 1
                        dup_dict[s[inner]].append(inner)
                        inner += 1
                        curr_sub_len = inner - outer
                    
                # inner += 1
                if curr_sub_len > sub_len:
                    sub_len = curr_sub_len

        return (sub_len)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("tmmzuxt"))
