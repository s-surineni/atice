from ppython.goodrich_algo.exceptions import Empty


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def is_empty(self):
        return self._size == 0

    def enqueue(self, el):
        if self._size == len(self):
            self._resize()

        avail = (self._front + self._size) % len(self)
        self._data[avail] = el
        self._size += 1

    def deque(self):
        if self._size == 0:
            raise Empty

        resp = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self)
        self._size -= 1
        return resp

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)


# if __file__ == '__main__':
if True:
    aq = ArrayQueue()
    aq.enqueue(7)
    aq.enqueue(3)
    aq.enqueue(8)
    print(aq)
    print(aq.deque())
    print(aq.deque())
    print(aq.deque())
    print(aq.deque())
