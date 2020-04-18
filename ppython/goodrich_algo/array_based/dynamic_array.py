import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._data = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def append(self, val):
        if self._n == self._capacity:
            self._resize()
        self._data[self._n] = val
        self._n += 1

    def _resize(self):
        new_arr = self._make_array(2 * self._capacity)
        for idx in range(self._n):
            new_arr[idx] = self._data[idx]

        self._data = new_arr
        self._capacity = 2 * self._capacity

    def __getitem__(self, idx):
        return self._data[idx]


if __name__ == '__main__':
    a_list = DynamicArray()
    a_list.append(4)
    a_list.append(7)
