root = None


class Node():
    def __init__(self, val):
        self.val = val
        self.p = self.l = self.r = None


def insert(node):
    global root
    nex = root
    now = None
    while nex:
        now = root
        if now.val >= node.val:
            nex = now.r
        else:
            nex = now.l
    if now:
        root = node
    elif now.val >= node.val:
        now.r = node
    else:
        now.l = node


options = {
    'i': insert
}

while(True):
    print('*'*80)
    print('Enter')
    print('i for insert')
    chose = raw_input()
    if options.get(chose):
        options[chose]()
