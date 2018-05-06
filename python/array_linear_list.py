from change_arr_len import ChangeArrayLength
from linear_list import LinearList


class ArrayLinearList(LinearList):
    def __init__(self, init_cap=10):
        if init_cap < 1:
            raise ValueError('Capacity cannot be < 1')

        self.element = [None] * init_cap
        self.cap = 0

    def is_empty(self):
        return self.cap == 0

    def size(self):
        return self.cap

    def check_index(self, idx):
        if idx < 0 or idx >= self.cap:
            raise IndexError('Index = {0} size = {1}'.format(
                idx, self.cap))

    def get(self, idx):
        self.check_index(idx)
        return self.element[idx]

    def index_of(self, ele):
        for trk in range(self.cap):
            if self.element[trk] == ele:
                return trk

        return -1

    def remove(self, idx):
        self.check_index(idx)
        removed_ele = self.element[idx]
        for trk in range(idx, (self.cap - 1)):
            self.element[trk] = self.element[trk + 1]

        self.cap -= 1
        self.element[self.cap] = None
        return removed_ele

    def add(self, idx, ele):
        if idx < 0 or idx > self.cap:
            raise IndexError('Index = {0} cap = {1}'.format(
                idx, self.cap))

        if self.cap == len(self.element):
            self.element = ChangeArrayLength.change_len_1D(self.element,
                                                           2 * self.cap)

        for trk in range(self.cap - 1, idx - 1, -1):
            self.element[trk + 1] = self.element[trk]

        self.element[idx] = ele
        self.cap += 1

    def __str__(self):
        list_str = '[ '
        for trk in range(self.cap):
            list_str += str(self.element[trk]) + ' '

        list_str += ']'
        return list_str


if __name__ == '__main__':
    linear_list = ArrayLinearList()
    print('Initial size is ' + str(linear_list.size()))

    if linear_list.is_empty():
        print('The list is empty')
    else:
        print('The list is not empty')

    linear_list.add(0, 2)
    print(linear_list)
    linear_list.add(1, 6)
    print(linear_list)
    linear_list.add(0, 1)
    print(linear_list)
    linear_list.add(2, 4)
    print('List size is ' + str(linear_list.size()))
    print('The list is ' + str(linear_list))
