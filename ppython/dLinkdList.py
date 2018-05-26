head = None


class Node:
    def __init__(self, value):
        self.value = value
        self.pre = None
        self.post = None


def insert():
    global head
    value = raw_input('insert the value for the node')
    if not head:
        head = Node(value)
    else:
        currNode = Node(value)
        head.pre = currNode
        currNode.post = head
        head = currNode


def search():
    value = raw_input('insert the value')
    currNode = head
    while currNode.post:
        if currNode.value == value:
            print 'value found'
            return currNode
        currNode = currNode.post
    if currNode.value == value:
        print ('value found')
        return currNode
    print('value not found')


def delete():
    global head
    node = search()
    if node.pre:
        node.pre.post = node.post
    else:
        head = node.post
    if node.post:
        node.post.pre = node.pre
    node.post = None
    node.pre = None


def display():
    currNode = head
    while currNode.post:
        print(currNode.value)
        currNode = currNode.post
    print(currNode.value)


chooser = {
    'i': insert,
    'd': display,
    's': search,
    'r': delete
}


def menu():
    while True:
        print
        print('*'*80)
        print('i to insert')
        print('d to display')
        print('s to search')
        print('r to delete')
        print('e to exit')
        print('*'*80)
        option = raw_input()
        if chooser.get(option):
            chooser[option]()
        elif option == 'e':
            break


menu()
