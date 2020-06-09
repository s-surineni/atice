'''
run this from
goodrich_algo
with command
python -m linked_lists.linked_stack
'''
from exceptions import Empty


class LinkedStack:

    class _Node:
        __slots__ = '_ele', '_nxt'
        def __init__(self, ele, nxt):
            self._ele = ele
            self._nxt = nxt

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Empty()
        return self.head._ele

    def push(self, ele):
        self._head = self._Node(ele, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty()
        ele = self._head._ele
        self._head = self._head._nxt
        self._size -= 1
        return ele


if __name__ == '__main__':
    ls = LinkedStack()
    ls.push(2)
    ls.push(3)
    ls.push(4)
    ls.push(5)
    print(ls.pop())
    print(ls.pop())
