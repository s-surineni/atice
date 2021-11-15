# https://leetcode.com/problems/iterator-for-combination/
class CombinationIterator:
    def __init__(self, characters, combinationLength):
        self.characters = characters
        self.combinationLength = combinationLength
        self.gen = self._next()
        self.next_val = None

    def next(self):
        if self.next_val:
            temp = self.next_val
            self.next_val = None
            return temp
        else:
            return next(self.gen)

    def hasNext(self):
        if self.next_val:
            return True
        else:
            try:
                self.next_val = next(self.gen)
                return True
            except StopIteration:
                return False

    def _next(self):
        charlen = len(self.characters)
        decnum = 0
        # (Better) to calculate decnum made up of 111 could have done (1 << 4 - 1)
        for po in range(charlen):
            decnum += 2 ** po
        # print("*" * 80)
        # print("ironman decnum", decnum)
        for val in range(decnum + 1):
            idx_loc = 0
            one_loc = []
            strn = ""
            while val:
                if val & (1):
                    # (Better) could have collected chars here only instead of storing them in an array
                    one_loc.append(idx_loc)
                idx_loc += 1
                val >>= 1
            if len(one_loc) == self.combinationLength:
                for oneidx in one_loc:
                    # strn += self.characters[len(self.characters) - oneidx - 1]
                    strn += self.characters[oneidx]

                yield strn


chars = "abc"
comblen = 2
ci = CombinationIterator(chars, comblen)
# gen = ci.next()
# print(next(gen))
# print(next(gen))
# print(next(gen))
print(ci.next())
print(ci.hasNext())
print(ci.next())
print(ci.hasNext())
print(ci.next())
print(ci.hasNext())
