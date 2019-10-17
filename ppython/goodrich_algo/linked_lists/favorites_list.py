from positional_list import PositionalList


class FavoritesList:

    def __init__(self):
        self._data = PositionalList()

    class _Item:
        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        walk = self._data.get_first()
        while walk is not None and walk.get_element() != e:
            walk = self._data.get_after_node(walk)
        return walk

    def _move_up(self, p):      # Different from the one in the book must test it
        if p == self._data.get_first():
            return
        count = p.get_element()._count
        new_p = self._data.get_before_node(p)
        while new_p != self._data.get_first() and count < new_p.get_element()._count:
            new_p = self._data.get_before_node(new_p)
        self._data.add_before(new_p, self._data.delete(p))

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        walk = self._find_position(e)
        if not walk:            # in book it is writtedn as walk is None. Why did they use it?
            walk = self._data.add_last(self._Item(e))
        walk.get_element()._count += 1
        self._move_up(walk)

    def remove(self, e):
        p = self._find_position(e)
        if p:
            self._data.delete(p)

    def top(self, k):

        if k > len(self._data):
            raise ValueError("Illegal value for k")

        p = self._data.get_first()

        for idx in range(k):
            yield p.get_element()._value
            p = self._data.get_after_node(p)


if __name__ == '__main__':
    f = FavoritesList()
    f.access('i')
    f.access('l')
    f.access('o')

    for e in f.top(3):
        print(e)
