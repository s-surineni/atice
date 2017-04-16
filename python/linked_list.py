class ChainNode():
    def __init__(self, ele, nxt):
        self.ele = ele
        self.nxt = nxt

ChainNode(None, None)


class Chain():

    def __init__(self):
        self.first_node = None
        self.list_size = 0

    def __init__(self, source_list):
        self.list_size = source_list.list_size

        if self.list_size == 0:
            self.first_node = None
            return

        src_node = source_list.first_node
        self.first_node = ChainNode(src_node.ele, None)
        src_node = src_node.next
        target_node = self.first_node

        while ! src_node:
            target_node.nxt = ChainNode(src_node.ele, None)
            target_node = target_node.nxt
            src_node = src_node.nxt

        target_node.nxt = None

    def check_index(self, idx):
        return 0 <= idx <= self.list_size

    def empty():
        return list_size == 0

    def size():
        return list_size

    def get(self, index):
        if check_index:
            current_node = self.first_node
            idx = 0

            while idx != index:
                current_node = current_node.nxt
                idx += 1

            return current_node.ele

    def index_of(self, ele):
        current_node = this.first_node
        idx = 0

        while current_node and current_node.ele != ele:
            current_node = current_node.nxt
            idx += 1
            
        if current_node:
            return idx
        else:
            return None

    def erase(self, index):
        if check_index(index):
            if index == 0:
                self.first_node = self.first_node.nxt
        pass

    def insert(index, ele):
        pass

    def output():
        pass
