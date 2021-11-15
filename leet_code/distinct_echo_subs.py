class Solution(object):
    def distinctEchoSubstrings(self, S):
        N = len(S)
        A = map(ord, S)
        MOD = 10 ** 9 + 7
        P = 37
        Pinv = pow(P, MOD-2, MOD)
        pwr = 1

        B = []
        for x in A:
            B.append(pwr * x % MOD)
            pwr *= P; pwr %= MOD

        Bsum = [0]
        for ha in B:
            Bsum.append( (Bsum[-1] +ha )% MOD)

        ppwr = 1
        ans = 0
        for length in xrange(1, N // 2 + 1):
            seen = set()
            ppwr *= P; ppwr %= MOD
            for i1 in xrange(N - 2 * length + 1):
                left = (Bsum[i1 + length] - Bsum[i1])
                left *= ppwr; left %= MOD
                right = (Bsum[i1 + length + length] - Bsum[i1 + length])
                right %= MOD
                if left == right:
                    seen.add(left * pow(Pinv, i1, MOD) % MOD)
                    #print("!", i1, length)
            #print("!!", length, len(seen))
            ans += len(seen)
        return ans
