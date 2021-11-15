class ChangeArrayLength:
    @staticmethod
    def change_len_1D(arr, new_len):
        n = len(arr)
        if n > new_len:
            raise ValueError

        new_arr = [] * new_len

        for trk in range(n):
            new_arr[trk] = arr[trk]
        return new_arr
