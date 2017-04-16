from __future__ import print_function

class ChainNode():
    def __init__(self, ele, nxt):
        self.ele = ele
        self.nxt = nxt

ChainNode(None, None)


class Chain():

    def __init__(self, source_list = None):

        if not source_list:
            self.first_node = None
            self.list_size = 0
            return
        
        self.list_size = source_list.list_size

        if self.list_size == 0:
            self.first_node = None
            return

        src_node = source_list.first_node
        self.first_node = ChainNode(src_node.ele, None)
        src_node = src_node.next
        target_node = self.first_node

        while not src_node:
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
            else:
                prev_node = self.first_node
                for trk in range(index):
                    prev_node = prev_node.nxt
                prev_node.nxt = prev_node.nxt.nxt
            self.list_size -= 1
                
                    
    def insert(self, index = None, ele = None):
        
        if index < 0 or index > self.list_size + 1:
            print("wont be able to insert")
            return
        
        if index == 0:
            self.first_node = ChainNode(ele, self.first_node)
            # print('first_node ', first_node)
            # print()
        else:
            prev_node = self.first_node
            for trk in range(index):
                prev_node = prev_node.nxt
                # see here we are doing initialization and
                # assigning next in the constructor itself
            prev_node.nxt = ChainNode(ele, prev_node.nxt)

    def output(self):
        curr_node = self.first_node
        # print('curr_node', curr_node)
        # print()
        while curr_node != None:
            print(curr_node.ele, end = ' ')
            # print()
            curr_node = curr_node.nxt
        print()

chain = Chain()

def inserter():
        print('please insert index and element')
        print()
        index, ele = raw_input().split(' ')
        index = int(index)
        # print(' index', index)
        ele = int(ele)
        chain.insert(index, ele)
        
menu = {
    'c': chain.check_index,
    's': chain.size,
    'g': chain.get,
    'in': chain.index_of,
    'e': chain.erase,
    'i': inserter,
    'o': chain.output
}



while(True):
    print('c for check_index')
    print('s  for chain size')
    print('g  for get')
    print('in for index of')
    print('e for erase')
    print('i for insert')
    print('o for output')
    choice = raw_input('please choose one of the above choice: ')
    if choice == 'x':
        break
    menu[choice]()
