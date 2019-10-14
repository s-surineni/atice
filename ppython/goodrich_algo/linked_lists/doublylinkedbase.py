class _DoublyLinkedBase:
    class _Node:
        def __init__(self, element, nxt, prev):
            self._nxt = nxt
            self._prev = prev
            self._element = element

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._nxt = self._trailer  # is it ok to access _nxt like this?
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, predecessor, successor)
        predecessor._nxt = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        node._prev._nxt = node._nxt
        node._nxt._prev = node._prev
        self._size -= 1
        element = node.element
        node._nxt = node._prev = node.element = None
        return element
