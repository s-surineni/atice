class MaxHeap:

    def __init__(self, arr):
        self.heap_size = len(arr)
        self.arr = arr

    def max_heapify(self, i):
        l_c_i = (2 * i) + 1
        r_c_i = (2 * i) + 2
        # here we are using another variable to hold the largest of two, this is one more way to compare largest of three
        if l_c_i < self.heap_size and self.arr[i] < self.arr[l_c_i]:
            largest_i = l_c_i
        else:
            largest_i = i
        if r_c_i < self.heap_size and self.arr[largest_i] < self.arr[r_c_i]:
            largest_i = r_c_i
        if largest_i != i:
            self.arr[largest_i], self.arr[i] = self.arr[i], self.arr[largest_i]
            self.max_heapify(largest_i)

    def build_max_heap(self):
        self.heap_size = len(self.arr)

        print('before', self.arr)
        for idx in range(((self.heap_size // 2) - 1), -1, -1):
            self.max_heapify(idx)
            print('iteratative', self.arr)

    def __str__(self):
        return str(self.arr)


if __name__ == '__main__':
    max_heap = MaxHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    max_heap.build_max_heap()
    print(max_heap)


class MinHeap:
    def __init__(self, arr):
        self.heap_size = len(arr)
        self.arr = arr

    def min_heapify(self, i):
        l_c_i = (2 * i) + 1
        r_c_i = (2 * i) + 2

        if l_c_i < self.heap_size and self.arr[i] > self.arr[l_c_i]:
            smallest = l_c_i
        else:
            smallest = i
        if r_c_i < self.heap_size and self.arr[smallest] > self.arr[r_c_i]:
            smallest = r_c_i
        if smallest 1= i:
            self.arr[smallest_i], self.arr[i] = self.arr[i], self.arr[smallest_i]
            self.min_heapify(smallest)

    def build_min_heap(self):
        for idx in range(((self.heap_size // 2) -1), -1, -1):
            self.min_heapify(idx)

    def __str__(self):
        return str(self.arr)
