from .abstract_priority_queue import PriorityQueueBase


class HeapPrioriryQueue(PriorityQueueBase):
    def __init__(self, contents=()):
        self._data = [self._Item(k, v) for k, v in contents]
        if self._data:
            self._heapify()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)

    def _heapify(self):
        start = (len(self._data) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def _upheap(self, j):
        parent = self._get_parent(j)

        if j > 0 and self._data[parent] > self._data[j]:
            self._swap(j, parent)
            self._upheap(parent)

    def _get_parent(self, j):
        return (j - 1) // 2

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _get_left_i(self, j):
        return (2 * j) + 1

    def _get_right_i(self, j):
        return (2 * j) + 2

    def _has_left(self, j):
        return ((2 * j) + 1) < len(self._data)

    def _has_right(self, j):
        return ((2 * j) + 2) < len(self._data)

    def _downheap(self, j):
        if self._has_left(j):
            left_i = self._get_left_i(j)
            smallest_child_i = left_i
            if self._has_right(j):
                right_i = self._get_right_i(j)
                if self._data[left_i] > self._data[right_i]:
                    smallest_child_i = right_i
            if self._data[smallest_child_i] < self._data[j]:
                self._swap(smallest_child_i, j)
                self._downheap(smallest_child_i)


if __name__ == '__main__':
    hpq = HeapPrioriryQueue()
    hpq.add(1, 'o')
    hpq.add(5, 'f')
    hpq.add(3, 't')
    print(hpq.remove_min())
    print(hpq.remove_min())
    hpq2 = HeapPrioriryQueue([(2, 't'), (8, 'e'), (6, 'e')])
    print(hpq2.remove_min())
