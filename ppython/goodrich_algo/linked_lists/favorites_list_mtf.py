from positional_list import PositionalList
from favorites_list import FavoritesList


class FavoritesListMTF(FavoritesList):
    def _move_up(self, p):
        if p != self._data.get_first():
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        if 1 > k > len(self):   # different to what given in book need to try
            raise ValueError('Illegal value for k')

        temp = PositionalList()

        for item in self._data:
            temp.add_last(item)

        for idx in range(k):
            current_top = temp.get_first()
            walk = temp.get_after_node(current_top)
            while walk:
                if walk.get_element()._count > current_top.get_element()._count:
                    current_top = walk
                walk = temp.get_after_node(walk)
            e = temp.delete(current_top)
            yield e._value


if __name__ == '__main__':
    fl = FavoritesListMTF()
    fl.access(5)
    fl.access(7)
    for it in fl.top(1):
        print(it)
    fl.access(2)
    for it in fl.top(3):
        print(it)
