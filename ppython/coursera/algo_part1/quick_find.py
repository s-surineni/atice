class QuickFindUF:
    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.id_arr = []
        for v in range(self.num_of_v):
            self.id_arr.append(v)

    def connected(self, p, q):
        return self.id_arr[p] == self.id_arr[q]

    def union(self, p, q):
        pid = self.id_arr[p]
        qid = self.id_arr[q]

        for idx in range(len(self.id_arr)):
            if self.id_arr[idx] == pid:
                self.id_arr[idx] = qid
                print('inside union if')
        print(self.id_arr)


def read_input():
    vertices = int(input().strip())
    print(vertices)
    uf = QuickFindUF(vertices)
    edge = list(map(int, input().split()))
    print(edge)
    try:
        while edge:
            p, q = edge

            if not uf.connected(p, q):
                print('in not connected')
                uf.union(p, q)
            edge = list(map(int, input().split()))
            print(edge)
    except EOFError:
        pass
    print(uf.id_arr)


read_input()
