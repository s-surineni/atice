class Solution:
    def minInsertions(self, s: str) -> int:
        d={}
        def dp(l,r):
            if l>=r:return 0
            if (l,r) not in d:
                d[(l,r)]=dp(l+1,r-1) if s[l]==s[r] else 1+min(dp(l+1,r),dp(l,r-1))
            return d[(l,r)]
        return dp(0,len(s)-1)
        return dp[0][n-1]


print(Solution().minInsertions("mbadm"))