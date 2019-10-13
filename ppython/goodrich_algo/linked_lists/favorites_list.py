class FavoritesList:
    class _Item:
        def __init__(self, e):
            self.value = e
            self.count = 0

    def _find_position(self, e):
        walk = self._data.get_first_node()
