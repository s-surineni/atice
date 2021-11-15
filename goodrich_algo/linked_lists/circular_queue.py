'''
run this from
goodrich_algo
with command
python -m linked_lists.circular_queue
'''


from exceptions import Empty


class CircularQueue:
    class _Node:
        __slots__ = '_ele', '_nxt'

        def __init__(self, ele, nxt=None):
            self._ele = ele
            self._nxt = nxt

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        cq = []
        curr = self._tail._nxt
        for _ in range(self._size):
            cq.append(curr._ele)
            curr = curr._nxt
        return str(cq)

    def empty(self):
        return self._size == 0

    def enqueue(self, ele):
        new_node = self._Node(ele)
        if self.empty():
            new_node._nxt = new_node
        else:
            new_node._nxt = self._tail._nxt
            self._tail._nxt = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.empty():
            raise Empty
        old_head = self._tail._nxt
        if self._size == 1:
            self._tail = None
        else:
            self._tail._nxt = old_head._nxt
        self._size -= 1
        return old_head._ele

    def first(self):
        if self.empty():
            raise Empty
        return self.tail._nxt._ele

    def rotate(self):
        if self.empty():
            raise Empty
        self._tail = self._tail._nxt


if __name__ == '__main__':
    cq = CircularQueue()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.enqueue(6)
    print(cq)
    cq.rotate()
    print('after rotate', cq)
    cq.dequeue()
    print('after dequeue', cq)
