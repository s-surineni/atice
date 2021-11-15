import sys
infi = sys.maxsize


def merge_sort_recur(arr, low, hi):
    if low < hi:
        div = (low + hi) // 2
        merge_sort_recur(arr, low, div)
        merge_sort_recur(arr, div + 1, hi)
        # low_half = [0] * ((div - low) + 1)
        # up_haof = [0] * (hi - div)
        low_half = arr[low:div + 1]
        low_half.append(infi)
        up_half = arr[div + 1:hi + 1]
        up_half.append(infi)
        lo_idx = 0
        up_idx = 0
        for idx in range(low, hi + 1):
            if low_half[lo_idx] < up_half[up_idx]:
                arr[idx] = low_half[lo_idx]
                lo_idx += 1
            else:
                arr[idx] = up_half[up_idx]
                up_idx += 1


def merge_sort(arr):
    merge_sort_recur(arr, 0, len(arr) - 1)


# arr = [5, 2, 3, 8, 1]
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print(arr)
