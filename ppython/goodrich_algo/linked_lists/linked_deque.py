import _DoublyLinkedBase from doublylinkedbase


class LinkedDeque(_DoublyLinkedBase):
    def get_first_element(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._nxt._element

    def get_last_element(self):
        if self._is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def 
