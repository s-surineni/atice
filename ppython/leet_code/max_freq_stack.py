import collections


class FreqStack:

    def __init__(self):
        self.max_freq = 0
        self.ele_freq = collections.Counter()
        self.groups = collections.defaultdict(list)

    def push(self, x: int) -> None:
        self.ele_freq[x] += 1
        x_freq = self.ele_freq[x]
        self.groups[x_freq].append(x)
        if x_freq > self.max_freq:
            self.max_freq = x_freq

    def pop(self) -> int:
        if not self.max_freq:
            return
        ret_ele = self.groups[self.max_freq].pop()
        self.ele_freq[ret_ele] -= 1
        if not self.groups[self.max_freq]:
            self.max_freq -= 1
        return ret_ele

fr = FreqStack()
fr.push(4)
fr.push(0)
fr.push(9)
fr.push(3)
fr.push(4)
fr.push(2)
fr.pop()
fr.push(6)
fr.pop()
fr.push(1)
fr.pop()
fr.push(1)
fr.pop()
fr.push(4)
fr.pop()
fr.pop()
fr.pop()
fr.pop()
fr.pop()
fr.pop()
