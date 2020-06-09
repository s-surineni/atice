from exceptions import Empty


class LinkedQueue:
    class _Node:
        __slots__ = '_ele', '_nxt'
        def __init__(self, ele, nxt=None):
            self._ele = ele
            self._nxt = nxt

    def __init__(self):
        self._size = 0
        self._head = self._tail = None

    def enqueue(self, ele):
        newest = self._Node(ele)
        if not self._head:
            self._head = newest
        else:
            self._tail._nxt = newest
        self._tail = newest
        self._size += 1

    def is_empty(self):
        return self._size == 0

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        removed = self._head._ele
        self._head = self._head._nxt
        self._size -= 1

        if self.is_empty():
            self._tail = None
        return removed

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._ele
