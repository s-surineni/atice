# python -m priority_queues.unsorted_priority_queue
# from goodrich_algo folder

from .abstract_priority_queue import PriorityQueueBase
from linked_lists.positional_list import PositionalList


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty')
        small = self._data.get_first()
        walk = self._data.get_after_node(small)

        while walk:
            if small.get_element() > walk.get_element():
                small = walk

            walk = self._data.get_after_node(walk)
        return small

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def get_min(self):
        p = self._find_min()
        item = p.get_element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._element)
