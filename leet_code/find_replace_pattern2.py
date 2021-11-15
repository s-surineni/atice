def findAndReplacePattern(words, p):
    def F(w):
        m = {}

        resp = [m.setdefault(c, len(m)) for c in w]
        print(resp)
        return resp
    return [w for w in words if F(w) == F(p)]


words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
findAndReplacePattern(words, pattern)
