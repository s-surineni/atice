class LinkedList:
    class _Node:
        def __init__(self, ele, nxt=None):
            self._ele = ele
            self._nxt = nxt

    def __init__(self):
        self._head = None

    def add_node(self, ele):
        new_node = self._Node(ele, self._head)
        self._head = new_node

    def find_loop(self):
        slow_p = fast_p = self._head
        # <!note> must not use pointer._nxt because if linked list is empty
        # we'll get an exception
        # while slow_p._nxt and fast_p._nxt:
        while slow_p and fast_p and fast_p._nxt:
            slow_p = slow_p._nxt
            fast_p = fast_p._nxt._nxt
            # <!note> doesn't need this as we checked this in while statement
            # if fast_p._nxt:
            #     fast_p = fast_p._nxt
            # else:
            #     return False
            if slow_p == fast_p:
                return True
        return False

    def find_remove_loop(self):
        slow_p = self._head
        fast_p = slow_p

        while slow_p and fast_p and fast_p._nxt:
            slow_p = slow_p._nxt
            fast_p = fast_p._nxt._nxt
            if slow_p == fast_p:
                break
        else:
            return False
        slow_p = self._head
        # <!note> <!better> by comparing next pointers we need not find out
        # last pointer separately
        while slow_p._nxt != fast_p._nxt:
            slow_p = slow_p._nxt
            fast_p = fast_p._nxt

        fast_p._nxt = None
        return True

    def __str__(self):
        ll_str = []
        po = ll._head
        while po:
            ll_str.append(str(po._ele))
            po = po._nxt
        return ' -> '.join(ll_str)


if __name__ == '__main__':
    ll = LinkedList()
    ll.add_node(1)
    ll.add_node(2)
    ll.add_node(3)
    ll.add_node(4)
    ll.add_node(5)
    ll.add_node(6)
    ll.add_node(7)
    ll.add_node(8)
    ll.add_node(9)
    print(ll)
    ll._head._nxt._nxt._nxt._nxt._nxt._nxt = ll._head._nxt._nxt
    # print(ll)
    # print(ll.find_loop())
    print(ll.find_remove_loop())
    print(ll)
