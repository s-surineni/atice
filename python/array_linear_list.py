from linear_list import LinearList


class ArrayLinerLinst(LinearList):
    def __init__(self, init_cap=10):
        if init_cap < 1:
            raise ValueError('Capacity cannot be < 1')

        self.element = [] * init_cap

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def check_index(self, idx):
        if idx < 0 or idx >= self.size:
            raise IndexError('Index = {0} size = {1}'.format(
                idx, self.size))

    def get(self, idx):
        self.check_index(idx)
        return self.element[idx]

    def index_of(self, ele):
        for trk in range(self.size):
            if self.element[trk] == ele:
                return trk

        return -1

    def remove(self, idx):
        self.check_index(idx)
        removed_ele = self.element[idx]
        for trk in range(idx, (self.size - 1)):
            self.element[trk] = self.element[trk + 1]

        self.size -= 1
        self.element[self.size] = None
        return removed_ele

    def add(self, idx, ele):
        if idx < 0 or idx > self.size:
            raise IndexError('Index = {0} size = {1}'.format(
                idx, self.size))

        if self.size == len(self.element):
            self.element = ChangeArrayLength.change_len_1D(self.element,
                                                           2 * self.size)
