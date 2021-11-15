from .positional_list import PositionalList


class FavoritesList:

    def __init__(self):
        self._data = PositionalList()

    def __str__(self):
        resp = ''
        for el in self._data:
            resp = resp + ' value: {} count: {},'.format(el._value, el._count)
        return resp

    class _Item:
        def __init__(self, e):
            self._value = e
            self._count = 0

    def _find_position(self, e):
        walk = self._data.get_first()
        while walk is not None and walk.get_element()._value != e:
            walk = self._data.get_after_node(walk)
        return walk

    def _move_up(self, p):      # Different from the one in the book must test it
        if p == self._data.get_first():
            return
        count = p.get_element()._count
        curr_p = self._data.get_before_node(p)
        while curr_p != self._data.get_first() and count > curr_p.get_element()._count:
            curr_p = self._data.get_before_node(curr_p)
        self._data.add_before(curr_p, self._data.delete(p))

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
    f.access('i')
    f.access('l')
    f.access('o')
    f.access('i')
    f.access('o')
    f.access('o')
    f.access('o')

    print(f)

    for e in f.top(3):
        print(e)
