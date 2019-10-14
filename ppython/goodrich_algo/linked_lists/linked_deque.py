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

    def insert_first(self, e):
        self._insert_between(e, self._header, self.header._nxt)

    def insert_last(self, e):
        self.insert_between(e, self._trailer.prev, self.trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._header._nxt)

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        self._delete_node(self._trailer._prev)
