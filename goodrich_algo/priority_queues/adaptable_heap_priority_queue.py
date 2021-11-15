from .heap_priority_queue import HeapPrioriryQueue


class AdaptableHeapPriorityQueue(HeapPrioriryQueue):
    class Locator(HeapPrioriryQueue._Item):
        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i] = j
        self._data[j] = i

    def _bubble(self, j):
        if j > 0 and self._data(j) < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, k, v):
        token = self.Locator(k, v, len(self._data))
        self._upheap(self.len(_data) - 1)
        return token

    def update(self, loc, new_key, new_val):
        j = loc._index

        if not(0<= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = new_key
        loc._value = new_val
        self._bubble(j)

    def remove(self, loc):
        j = loc._index
        if not(0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)
