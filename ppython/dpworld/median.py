import bisect


class MedianCalculator:
    def __init__(self):
        self._data = []

    def add_num(self, val):
        bisect.insort(self._data, val)

    def find_median(self):
        data_len = len(self._data)
        if data_len % 2:  # this will be true if len is odd
            return self._data[data_len // 2]
        else:
            return (self._data[data_len // 2] + self._data[(data_len - 1) // 2]) / 2
