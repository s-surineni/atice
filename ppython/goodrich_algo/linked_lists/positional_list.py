from doublylinkedbase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def get_element(self):
            return self._node._element

        def __eq__(self, other):
            # return (type(self) is type(other) and self._node is other._node)
            return (self._container is other._container and self._node is other._node)

        def __ne__(self, other):
            return  not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be propoer Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._nxt is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def get_first(self):
        return self._make_position(self._header._nxt)

    def get_last(self):
        return self._make_position(self._trailer._prev)

    def get_before_node(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def get_after_node(self, p):
        node = self._validate(p)
        return self._make_position(node._nxt)

    def __iter__(self):
        cursor = self.get_first()
        while cursor is not None:
            yield cursor.get_element()
            cursor = self.get_after_node(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._nxt)  # header and trailers are still only nodes and not positions?

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_after(self, p, e):
        original = self._validate(p)  # !getting node first not using the passed position
        return self._insert_between(e, original, original._nxt)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        node = self._validate(p)
        old_value = node._element
        node._element = e
        return old_value


if __name__ == '__main__':
    p = PositionalList()
